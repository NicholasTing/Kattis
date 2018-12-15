range1, range2 = map(int,input().split(" "))

def divide(numbers):

    number_list = list(map(int,str(numbers)))

    if(len(set(number_list))) != 6:
        return 0
        
    for number in number_list:
        if number == 0:
            return 0
        elif numbers % number != 0:
            return 0
        
    return 1

total = 0

for i in range(range1,range2):

    total += divide(i)
    divide(i)

print(total)