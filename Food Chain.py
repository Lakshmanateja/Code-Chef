t=int(input())
for i in range(t):
    x,k=map(int,input().split())
    count=0
    a=0
    while a!=0 or count==0:
        a=x//k
        count=count+1
        x=a
    print(count)    
