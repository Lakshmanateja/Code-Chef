t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    num=10*x
    if num<y:
        print(num*z)
    else:
        print(y*z)
