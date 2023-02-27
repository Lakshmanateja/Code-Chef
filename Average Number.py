t=int(input())
for i in range(t):
    n,k,v=map(int,input().split())
    list1=list(map(int,input().split()))
    sum1=sum(list1)
    n1=n+k
    ans=v*(n1)-sum1
    if ans>0 and ans%k==0:
        print(ans//k)
    else:
        print("-1")
