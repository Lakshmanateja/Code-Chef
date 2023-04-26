t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=x**4
    b=4*(y**2)
    c=4*(x**2)*y
    if a+b==c:
        print("Yes")
    else:
        print("No")
