#Coded by Jing Kun Ting
#Coded on 12/7/2018
#open.kattis.com problem : Soylent
#Problem : https://open.kattis.com/problems/soylent

import math
# Total number of inputs
total = int(input())

while total != 0:
    total_calories = int(input())
    if(total_calories < 400):
        print(1)
    else:
        print(math.ceil(total_calories / 400))
    total -= 1
