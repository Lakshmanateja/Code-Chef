t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y>x:
        print(x+(y-x)*2)
    else:
        print(y)
