t=int(input())
for i in range(t):
    a,b,c,x=map(int,input().split())
    if a+b>=x:
        print("YES")
    elif b+c>=x:
        print("YES")
    elif c+a>=x:
        print("YES")
    else:
        print("NO")
