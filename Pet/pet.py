#Coded by Jing Kun Ting
#Coded on 15/1/2018
#open.kattis.com problem : Pet

NUM_CONTESTANTS = 5
highest_contestant = 0
highest_points = 0
curr_contestant = 0

while curr_contestant < NUM_CONTESTANTS:
    points = sum(list(map(int,input().split())))

    if points > highest_points:
        highest_points = points
        highest_contestant = curr_contestant + 1

    curr_contestant += 1

print(str(highest_contestant) + " " + str(highest_points))
