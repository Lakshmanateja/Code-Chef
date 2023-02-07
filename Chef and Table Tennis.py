t=int(input())
for i in range(t):
    s=input()
    list1=[i for i in s]
    count0=0
    count1=0
    for j in range(len(list1)):
        if list1[j]=='0':
            count0=count0+1
        if list1[j]=='1':
            count1=count1+1
    
    if count0>count1:
        print("LOSE")
    else:
        print("WIN")
