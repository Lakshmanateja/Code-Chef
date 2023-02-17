t=int(input())
for i in range(t):
    list1=list(map(int,input().split()))
    if list1[0]==list1[2] and list1[1]==list1[3]:
            print(1)
    elif list1[0]==list1[3] and list1[1]==list1[2]:
            print(1)
            
    elif list1[0]==list1[4] and list1[1]==list1[5]:
            print(2)
    elif list1[0]==list1[5] and list1[1]==list1[4]:
            print(2)
    else:
        print(0)
