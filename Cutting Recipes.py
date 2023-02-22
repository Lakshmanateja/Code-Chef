import math
t=int(input())
for i in range(t):
    list1=list(map(int,input().split()))
    list2=list1[1:]
    n=list1[0]
    min1=min(list2)
    count=0
    div=math.gcd(list2[0],list2[1])
    for j in range(2,n):
        div=math.gcd(div,list2[j])
    for j in range(0,n):
        print(list2[j]//div,end=" ")
    print()    
    
            
