t=int(input())
for i in range(t):
    n,x,y=map(int,input().split())
    s=input()
    if "1" in s and "0" in s:
        x=min(x,y)
        print(x)
    else:
        print(0)
