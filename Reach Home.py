t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x*5>=y:
        print("Yes")
    else:
        print("No")
