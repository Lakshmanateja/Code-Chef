t=int(input())
for i in range(t):
    n = int(input())
    p = list(map(int,input().split()))
    m1 = p.index(1)
    mn = p.index(n)
    print(n - 1 - mn + m1 - int(m1>mn))
