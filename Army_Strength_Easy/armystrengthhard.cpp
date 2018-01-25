/** Coded by Jing Kun Ting
  * Coded on 25/1/2018
  * open.kattis.com problem : ArmyStrengthHard
  * Problem : https://open.kattis.com/problems/armystrengthhard
  * CPP Solution
*/


#include <bits/stdc++.h>

using namespace std;

int test_cases = 0;

int
main(){
    scanf("%d",&test_cases);

    int godz = 0;
    int mgodz = 0;

    while(test_cases--){
        //Godzilla wins if 0
        //MGodzilla wins if 1

        list<int> godz_army;
        list<int> mgodz_army;
        int army;

        scanf("%d %d",&godz,&mgodz);

        while(godz--){
            scanf("%d",&army);
            godz_army.push_back(army);
        }

        while(mgodz--){
            scanf("%d",&army);
            mgodz_army.push_back(army);
        }

        godz_army.sort();
        mgodz_army.sort();

        while(godz_army.size() !=0 && mgodz_army.size() != 0){
            if(godz_army.front() > mgodz_army.front()){
                mgodz_army.pop_front();
            }
            else if(mgodz_army.front() > godz_army.front()){
                godz_army.pop_front();
            }
            else if(mgodz_army.front() == mgodz_army.front()){
                mgodz_army.pop_front();
            }
        }

        if(godz_army.size() == 0){
            printf("MechaGodzilla\n");
        }
        else{
            printf("Godzilla\n");
        }

    }
    return 0;
}
