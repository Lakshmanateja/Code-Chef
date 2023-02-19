t=int(input())
for i in range(t):
    w1,w2,x1,x2,m=map(int,input().split())
    p=w2-w1
    x1=x1*m
    x2=x2*m
    if p>=x1 and p<=x2:
        print(1)
    else:
        print(0)
