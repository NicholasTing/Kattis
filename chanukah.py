num = int(input())

days = [0]
count = 2

total = 0

while count < 15000:
    total = total + count
    days.append(total)
    count += 1


while num != 0:

    a, day = map(int,input().split(" "))
    count = 0
    print(str(a) + " " + str(days[day]))

    num -= 1
