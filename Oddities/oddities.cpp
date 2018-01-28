/**Coded by Jing Kun Ting
*Coded on ?/?/17
*open.kattis.com problem : Oddities
*Problem : https://open.kattis.com/problems/oddities
*Coded in CPP
*/

#include <cstdio>
#include <cmath>

using namespace std;

int N;

int
main(){
    scanf("%d",&N);
    int num = 0;
    while(N--){
        scanf("%d",&num);
        if(num % 2 == 0){
            printf("%d is even\n",num);
        }
        else{
            printf("%d is odd\n",num);
        }
    }
    return 0;
}
