t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if y<=x and z<=x:
        print("PIZZA")
    elif z<=x:
        print("BURGER")
    elif y<=x:
        print("PIZZA")
    else:
        print("NOTHING")
