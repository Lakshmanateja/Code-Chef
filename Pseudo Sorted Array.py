t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    for j in range(n-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            break
    
    if list1==sorted(list1):
        print("Yes")
    else:
        print("No")
