def prime(a):
    if a%2==0:
        return 2
    elif a%3==0:
        return 3
    elif a%5==0:
        return 5
    elif a%7==0:
        return 7
        
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    count=0
    while x<y:
        if x%2==0:
            if (y-x)%2==0:
                count=count+(y-x)//2
            else:
                count=count+(y-x)//2+1
            break    
        x=x+prime(x)
        count=count+1
    print(count)    
