from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    x=Counter(list1)
    m=max(x.values())
    print(n-m)
