t=int(input())
for i in range(t):
    maxT,maxN,sumN=map(int,input().split())
    max=0
    for j in range(1,maxT+1):
        if j*maxN<=sumN:
            if j>max:
                max=j
    count=0            
    for j in range(max):
        count=count+(maxN*maxN)
    if (max*maxN)==sumN:
        print(count)
    else:
        if max+1<=maxT:
            p=sumN-(max*maxN)
            count=count+(p*p)
            print(count)
        else:
            print(count)
