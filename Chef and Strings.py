t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    count=0
    for j in range(len(list1)-1):
        count=count+(abs(list1[j]-list1[j+1]))-1
    print(count)    
