import math
total = int(input())

while total != 0:
    digit = int(input())    
    ans = math.factorial(digit)
    ans = str(ans)
    print(ans[-1])
    total -= 1