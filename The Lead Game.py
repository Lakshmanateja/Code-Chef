n=int(input())
p=q=r=s=0
for i in range(n):
    n,m=map(int,input().split())
    r=r+n
    s=s+m
    if r>s:
        p=max(p,(r-s))
    else:
        q=max(q,s-r)
if p>q:
    print("1 "+str(p))
else:
    print("2 "+str(q))
