t=int(input())
for i in range(t):
    n,a,b,c=map(int,input().split())
    if a+c>=n and b>=n:
        print("YES")
    else:
        print("NO")
