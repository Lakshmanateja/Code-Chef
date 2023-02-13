t=int(input())
for i in range(t):
    n,b=map(int,input().split())
    list1=[]
    list2=[]
    list3=[]
    for j in range(n):
        p,q,r=map(int,input().split())
        list1.append(p)
        list2.append(q)
        list3.append(r)
    a=0  
    list4=[]
    for j in range(n):
        if list3[j]<=b:
            list4.append(j)
    m=0
    for j in list4:
        if list1[j]*list2[j]>m:
            m=list1[j]*list2[j]
    
    if not list4:
        print("no tablet")
    else:
        print(m)
            
