t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    list1=list(map(int,input().split()))
    for i in range(n):
        if k>=list1[i]:
            print("1",end="")
            k=k-list1[i]
        else:
            print("0",end="")
    print()   
