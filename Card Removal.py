from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    x=Counter(list1)
    list2=list(x.values())
    max1=max(list2)
    print(n-max1)
