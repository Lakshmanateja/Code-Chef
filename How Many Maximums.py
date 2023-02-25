t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=0
    for i in range(0,n-2):
        if n==2 or n==1:
            count=1
            break
        if s[i]=='0' and s[i+1]=='1':
            count=count+1
    if s[0]=='1':
        count=count+1
    if s[n-2]=='0':
        count=count+1
    print(count)    
