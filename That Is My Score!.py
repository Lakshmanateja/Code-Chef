t=int(input())
for j in range(t):
    n=int(input())
    list1=[]
    list2=[]
    for i in range(n):
        x,y=map(int,input().split())
        list1.append(x)
        list2.append(y)
    list3=[0,0,0,0,0,0,0,0]    
    for i in range(len(list1)):
        if list1[i]>=1 and list1[i]<=8:
            if list3[list1[i]-1]<list2[i]:
                list3[list1[i]-1]=list2[i]
    print(sum(list3))       
