t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    m=100-a
    n=200-(2*b)
    if m>n:
        print("SECOND")
    elif m<n:
        print("FIRST")
    else:
        print("BOTH")
