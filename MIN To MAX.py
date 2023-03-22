from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    m=min(list1)
    x=Counter(list1)
    p=x[m]
    print(n-p)
