t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    list1.sort()
    count=0
    for j in range(0,n-1):
        if abs(list1[j]-list1[j+1])<=1:
            count=count+1
    if count==len(list1)-1:
        print("YES")
    else:
        print("NO")
