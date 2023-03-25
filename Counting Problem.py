t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    count=0
    for j in range(n):
        if list1[j]%2 != 0:
            count=count+1
    if count%2==0 and count!=0:
        print("Yes")
    else:
        print("No")
