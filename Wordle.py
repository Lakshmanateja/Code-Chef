t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    list1=[j for j in s1]
    list2=[j for j in s2]
    list3=[]
    for j in range(len(list1)):
        if list1[j]==list2[j]:
            list3.append("G")
        else:
            list3.append("B")
    for j in range(len(list3)):
        print(list3[j],end="")
    print()    
