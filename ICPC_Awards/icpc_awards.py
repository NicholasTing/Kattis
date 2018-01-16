#Coded by Jing Kun Ting
#Coded on 15/1/2018
#open.kattis.com problem : ICPC Awards
#Problem: https://open.kattis.com/problems/icpcawards
#Python 3 Solution

total_teams = int(input())
universities = []

while len(universities) < 12:

    data = input().split()

    uni = data[0]
    team = data[1]

    if uni not in universities:
        universities.append(uni)
        print(uni + " " + team)
