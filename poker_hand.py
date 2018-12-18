a,b,c,d,e = input().split(" ")

ans = [a[0],b[0],c[0],d[0],e[0]]
ans_list = list(set(ans))

highest = 0
temp = []
for dig in ans_list:
    check = 0
    for num in ans:
        if num == dig:
            check += 1
    
    if check > highest:
        highest = check

print(highest)
