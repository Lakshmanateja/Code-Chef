t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    list1.sort()
    count=0
    count1=0
    for j in range(1,n):
        if list1[j]==list1[j-1]:
            count=count+1
        else:
            count1=count1+1
    print(count1+1)        
