t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    count=0
    for j in range(0,n):
        sum1=0
        pro1=1
        for k in range(j,n):
            sum1=sum1+list1[k]
            pro1=pro1*list1[k]
            if sum1==pro1:
                count=count+1
    print(count)  
