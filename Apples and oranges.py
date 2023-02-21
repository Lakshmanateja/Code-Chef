import math
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    res=math.gcd(n,m)
    print(res)
