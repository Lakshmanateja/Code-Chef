t=int(input())
for i in range(t):
    n,a,b=(map(int,input().split()))
    half=n//2
    odd=n-half
    even=half
    print((odd*b)+(even*a))
