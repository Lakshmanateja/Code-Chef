t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    d=0
    for j in range(1,30):
        if (a^j)<(b^j) and (b^j)<(c^j):
            d=1
            break
        else:
            d=0
        
    if d==1:
        print(j)
    else:
        print(-1)
    
