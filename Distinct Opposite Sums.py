t=int(input())
for i in range(t):
    n=int(input())
    list1=[]
    for j in range(1,n+1):
        list1.append(j)
    list2=list1[0:n//2]
    list3=list1[n//2+1:n-1]
    list2.reverse()
    list2.extend(list1[n//2:])
    print(*list2)
