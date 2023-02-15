t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    p=min(b,c)
    b=b-p
    c=c-p
    p=min(a,c)
    a=a-p
    c=c-p
    p=min(a,b)
    a=a-p
    b=b-p
    if a>0:
        print("YES")
    else:
        print("NO")
