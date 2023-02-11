from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    x=Counter(list1)
    for j in x.keys():
        m=x[j]
        s=0
        if m>=3:
            s=1
            print("NO")
            break
        
    if s==0:
        print("YES")
