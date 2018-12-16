total = int(input())

ans = 0
while total != 0:
    a,b = input().split(" ")
    ans += float(a) * float(b)
    total -= 1

print("%.3f" % float(ans))