t=int(input())
for i in range(t):
    a,b,x=map(int,input().split())
    p=b-a
    count=0
    while(x*count<p):
        count=count+1
    print(count)  
