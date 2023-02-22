t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    list1=list(map(int,input().split()))
    list1.sort()
    print(list1[len(list1)-x]-1)
