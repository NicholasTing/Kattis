#include <cstdio>

using namespace std;

int
main(){
    int hour, minute;
    int ans_hour, ans_minute;
    scanf("%d %d",&hour, &minute);

    if(hour == 0){
        ans_hour = 23;
    }
    else{
        ans_hour = hour - 1;
    }

    if(minute < 45){
        ans_minute = 60 - (45-minute);
    }
    else if(minute == 45){
        if(hour == 0){
            printf("0 00");
        }
        else{
            printf("%d 00",ans_hour+1);
        }
        return 0;
    }
    else{
        ans_hour = ans_hour + 1;
        ans_minute = minute - 45;
    }

    printf("%d %d",ans_hour,ans_minute);
    return 0;
}
