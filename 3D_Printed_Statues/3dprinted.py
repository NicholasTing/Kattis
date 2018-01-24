#Coded by Jing Kun Ting
#Coded on 24/1/2018
#open.kattis.com problem : 3d printed statues
#Problem : https://open.kattis.com/problems/3dprinter
#Python 3 Solution

import math

printers = int(input())

total_days = math.log(printers,2)

print("{0:d}".format(int(math.ceil(total_days+1))))
