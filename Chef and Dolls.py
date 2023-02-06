t=int(input())
for i in range(t):
    n=int(input())
    list1=[]
    for j in range(n):
        n1=int(input())
        list1.append(n1)
    list1.sort()
    for j in range(0,n-1,2):
        if list1[j]!=list1[j+1]:
            print(list1[j])
            break
        if list1[n-1]!=list1[n-2]:
            print(list1[n-1])
            break
