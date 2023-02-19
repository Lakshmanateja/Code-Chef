t=int(input())
for i in range(t):
    s,a,b,c=map(int,input().split())
    s=(100+c)/100*s
    if s>=a and s<=b:
        print("Yes")
    else:
        print("No")
