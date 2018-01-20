#Coded by Jing Kun Ting
#Coded on 15/1/2018
#open.kattis.com problem : ABC
#Problem : https://open.kattis.com/problems/abc

abc = sorted(list(map(int,input().split())))
ABC = input()

def letter_comparator(letter):

    if letter == "A":
        return abc[0]

    elif letter == "B":
        return abc[1]

    else:
        return abc[2]

answer = ""

for letter in ABC:
    answer += str(letter_comparator(letter))
    answer += " "

print(answer)
