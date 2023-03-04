t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    count1=0
    count2=0
    
    j=1
    while(count1<=a and count2<=b):
        if j%2!=0:
            count1=count1+j
            j=j+1
        else:
            count2=count2+j
            j=j+1
    if count1>a:
        print("Bob")
    if count2>b:
        print("Limak")
