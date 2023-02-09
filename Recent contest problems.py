t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(str,input().split()))
    count1=0
    count2=0
    for j in range(n):
        if list1[j]=='START38':
            count1=count1+1
        if list1[j]=='LTIME108':
            count2=count2+1
    print(count1,end=" ")
    print(count2)
