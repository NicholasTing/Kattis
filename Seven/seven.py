#Coded by Jing Kun Ting
#Coded on 17/1/2018
#open.kattis.com problem : Seven Wonders
#Problem : https://open.kattis.com/problems/sevenwonders

char = input()
check = list(char)

t = []
g = []
c = []

for i in check:
    if i == 'T':
        t.append(i)
    elif i == 'G':
        g.append(i)
    else:
        c.append(i)

tot_t = len(t)
tot_g = len(g)
tot_c = len(c)

small = 0

if(tot_t != 0 and tot_g != 0 and tot_c != 0):
    small = min(len(t),len(g),len(c))

answer = tot_t ** 2 + tot_g ** 2 + tot_c ** 2 + small * 7
print(answer)
