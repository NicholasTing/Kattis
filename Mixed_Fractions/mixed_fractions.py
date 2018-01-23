#Coded by Jing Kun Ting
#Coded on 23/1/2018
#open.kattis.com problem : Mixed Fractions
#Problem : https://open.kattis.com/problems/mixedfractions
#Python 2 Solution

first,second = map(int,raw_input().split())

while(first != 0 and second != 0):
    whole = 0
    numerator = 0
    denominator = 0

    whole = first / second
    numerator = first % second
    denominator = second

    print("{0:d} {1:d} / {2:d}".format(whole,numerator,denominator))
    first,second = map(int,raw_input().split())
