#include <bits/stdc++.h>

/*
 * This functions check whether a num is a perfect num
*/
int
perfect_num(int num){
    int total = 1;
    int final_num = num;
    int half = sqrt(num);


    for(int i = 2;i < sqrt(num);i++){

        if(num%i == 0){
            total = total + i;
            total = total + (num/i);
        }
            // printf("i = %d, num = %d\n",i,num/i);
        // printf("total is %d\n",total);
    }

    // printf("%d is total\n",total);
    if(half * half == num){
        total += half;
    }


    if(total == final_num){
        return 1;
    }

    else if(total <= final_num + 2 && total >= final_num - 2){
        return 2;
    }

    else{
        return 0;
    }
}

int
main(){
    int num;
    int perfect;
    while(scanf("%d",&num) == 1){
        perfect = perfect_num(num);
        if(perfect == 1){
            printf("%d perfect",num);
        }
        else if(perfect == 2){
            printf("%d almost perfect",num);
        }
        else{
            printf("%d not perfect",num );
        }
        printf("\n");
    }
    return 0;
}
