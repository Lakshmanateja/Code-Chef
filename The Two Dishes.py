t=int(input())
for i in range(t):
    list1=[]
    n,s=map(int,input().split())
    m=s-n
    if s>n and s!=0:
        print(n-m)
    elif n>s and n!=0:
        print(s)
    else:
        print(n)
