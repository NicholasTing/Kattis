/**
  * Coded by Jing Kun Ting
  * Coded on X/X/2017
  * open.kattis.com problem : Sibice
  * Problem: https://open.kattis.com/problems/Sibice
  * Coded in CPP
*/

#include <cstdio>
#include <cmath>

int
main(){
    int N, W, H;
    scanf("%d %d %d",&N,&W,&H);
    float diagonal = 0;
    diagonal = sqrt(pow(W,2) + pow(H,2));
    int check;
    while(N--){
        scanf("%d",&check);
        if(check <= W || check <= H || check <= diagonal){
            printf("DA\n");
        }
        else{
            printf("NE\n");
        }
    }
    return 0;
}
