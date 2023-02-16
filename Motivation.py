t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    list1=[]
    list2=[]
    for j in range(n):
        gb,imdb=map(int,input().split())
        list1.append(gb)
        list2.append(imdb)
    max=0
    for j in range(len(list1)):
        if x>=list1[j]:
            m=list2[j]
            if m>max:
                max=m
    print(max)       
