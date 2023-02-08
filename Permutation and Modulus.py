t=int(input())
for i in range(t):
    n=int(input())
    list1=[]
    for j in range(1,n+1):
        list1.append(j)
    list1.remove(1)
    list1.append(1)
    for j in range(n):
        print(list1[j],end=" ")
    print()
