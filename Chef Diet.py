t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    list1=list(map(int,input().split()))
    count=0
    m=0
    for j in range(n):
        if list1[j]+count>=k:
            count=count+list1[j]-k
        else:
            m=j+1
            break
    if m:
        print("NO "+str(m))
    else:
        print("YES")
