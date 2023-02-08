t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=0
    list1=[j for j in s]
    for j in range(len(list1)):
        for k in range(j+1,len(list1)):
            if list1[j]==list1[k]:
                count=count+1
    
    if count>=1:
        print(len(s)-2)
    else:
        print(-1)
