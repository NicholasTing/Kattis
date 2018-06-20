/*
 * Coded by Jing Kun Ting
 * Student Number : 792 886
 * Coded on 14 - 04 - 2018
 *
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/stat.h>
#include <fcntl.h>

#define HTML 1
#define CSS 2
#define JS 3
#define JPG 4

#define CONNMAX 1000
#define BYTES 1024

/*
 *
 * Functions
 *
*/

//Find file type of a give argument
int find_file_type(char *file_name){

	char *JS_FILE = "js";
	char *CSS_FILE = "css";
	char *JPG_FILE = "jpg";
	char *HTML_FILE = "html";

	char *extension = strtok(file_name, ".");
	extension = strtok(NULL, ".");

	if(!strcmp(extension, HTML_FILE)){
		return HTML;
	}
	else if(!strcmp(extension, CSS_FILE)){
		return CSS;
	}
	else if(!strcmp(extension, JPG_FILE)){
		return JPG;
	}
	else if(!strcmp(extension, JS_FILE)){
		return JS;
	}

	return 0;

}

//First response function
void response_function(FILE* file_data, int newsockfd, int file_type, char *http_ver, char *path){

	char response_data[1024];
	char send_data[2048];
	char http_header[256];
	int bytes_read;
	char data_to_send[1024];
	int fd;

	strcpy(http_header,http_ver);
	printf("here %s is htp_header initially\n",http_ver);

	if(file_type == HTML){
		strcat(http_header," 200 OK\r\nContent-type: text/html\r\n\r\n");

		strcpy(send_data,http_header);
		printf("%s is the senddd \n",send_data);
		// write(newsockfd,send_data,strlen(send_data));
	}
	else if(file_type == CSS){
		printf("I am a css file");
		strcat(http_header," 200 OK\r\nContent-Type: text/css\r\n\r\n");

		strcpy(send_data,http_header);
		// write(newsockfd,send_data,strlen(send_data));
	}
	else if(file_type == JS){
		strcat(http_header," 200 OK\nContent-Type: text/javascript\n\n");

		strcpy(send_data,http_header);
		printf("%s is http header\n",http_header);
		printf("%s is sending things\n",send_data);
		printf("%lu is size of header\n",strlen(send_data));
		// write(newsockfd,send_data,strlen(send_data));
	}
	else if(file_type == JPG){
		strcat(http_header," 200 OK\nContent-Type: image/jpeg\n\n");
	}

	// while(fgets(response_data, sizeof(file_data), file_data) != NULL){

	// 	strcat(http_header, response_data);

	// }

	// while( (bytes_read = read(file_data, data_to_send, 1024)) > 0){
	// 	write(newsockfd,data_to_send,bytes_read);
	// }


	// if (send(newsockfd, http_header, sizeof(http_header), 0) == -1) {
	// 	perror("ERROR sending data to client");
	// 	exit(1);
	// }

	char length[2048];
	int bytes_length = 0;

	if ( (fd = open(path,O_RDONLY)) != -1){

		while ( (bytes_read = read(fd,data_to_send, 2048)) > 0){

			bytes_length = strlen(send_data) + bytes_read;
			strcat(send_data,data_to_send);
			write(newsockfd,send_data,bytes_length);

		}

	}

	// if (write(newsockfd, http_header,sizeof(http_header)) == -1){
	// 	perror("ERROR writing data");
	// 	exit(1);
	// }

}


int main(int argc, char *argv[]) {
	int sockfd, newsockfd, portno;// clilen;
	char buffer[2048];
	struct sockaddr_in serv_addr, cli_addr;
	socklen_t clilen;
	int n;

	if (argc < 3)
	{
		fprintf(stderr,"ERROR, no port provided\n");
		exit(1);
	}

	/* Create TCP socket */
	sockfd = socket(AF_INET, SOCK_STREAM, 0);

	if (sockfd < 0) {
		perror("ERROR opening socket");
		exit(1);
	}

	bzero((char *) &serv_addr, sizeof(serv_addr));

	// Port number
	portno = atoi(argv[1]);
	// The path to the directory

	/* Create address we're going to listen on (given port number)
	 - converted to network byte order & any IP address for
	 this machine */

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(portno);  // store in machine-neutral format

	 /* Bind the socket to our specified IP and port*/

	if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
	{
		perror("ERROR on binding");
		exit(1);
	}

	/* Listen on socket - means we're ready to accept connections -
	 incoming connection requests will be queued */

	listen(sockfd,5);

	clilen = sizeof(cli_addr);

	/* Accept a connection - block until a connection is ready to
	 be accepted. Get back a new file descriptor to communicate on. */

	newsockfd = accept(	sockfd, (struct sockaddr *) &cli_addr,
						&clilen);

	if (newsockfd < 0)
	{
		perror("ERROR on accept");
		exit(1);
	}

	bzero(buffer,2048);

	// we gonna receive stuffs from the new socket
	n = read(newsockfd, buffer, 2048);

	// didn't read anything
	if (n < 0) {
		perror("Error reading from socket\n");
		exit(1);
	}

	printf("%s is the buffer\n",buffer);

	char *version_number;
	char *p = strtok(buffer, " ");

	int file_type = 0;
	// get the path in the middle
	p = strtok(NULL, " ");

	version_number = strtok(NULL, "\n");

	char path[9999];

	FILE *file_data;
	strcpy(path,strcat(argv[2],p));

	printf("%s is path\n",path);
	file_data = fopen(path, "r");

	if(file_data == NULL){
		write(newsockfd, "HTTP/1.0 404 Not Found", sizeof("HTTP/1.0 404 Not Found"));
		exit(1);
	}

	file_type = find_file_type(p);

	response_function(file_data,newsockfd, file_type, "HTTP/1.0", path);
	/* close socket */

	close(sockfd);

	return 0;
}
