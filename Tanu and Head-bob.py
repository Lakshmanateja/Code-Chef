t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    cn=cy=ci=0
    for j in s:
        if j=='N':
            cn=cn+1
        if j=='Y':
            cy=cy+1
        if j=='I':
            ci=ci+1
    if ci>0:
        print("INDIAN")
    elif cy>0:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
