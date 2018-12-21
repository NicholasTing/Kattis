n,m = map(int,input().split(" "))

if m > n:
    if m - n != 1:
        print("Dr. Chaz will have " + str(m-n) +  " pieces of chicken left over!")
    
    else:
        print("Dr. Chaz will have 1 piece of chicken left over!")

else:

    if n-m != 1:
        print("Dr. Chaz needs " + str(n-m) + " more pieces of chicken!")
    
    else:
        print("Dr. Chaz needs 1 more piece of chicken!")
