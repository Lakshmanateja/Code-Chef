from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    b=input()
    x=Counter(b)
    n1=x['1']
    n0=x['0']
    m=120-n
    a=m+n1
    if (a/120)*100 >=75:
        print("YES")
    else:
        print("NO")
