n=int(input())
bs=[int(i) for i in input().strip().split()]
vis=[0]*n
c=int(input())
pt=c
f=0
if(0 not in bs):
    print("false")
else:
    pos=bs.index(0)
    while(pt!=pos and pt>=0 and pt<=n and vis[pt]!=1):
        if(pt<pos):
            vis[pt]=1
            pt=pt+bs[pt]
        elif(pt==pos):
            f=1
            break
        elif(pt>pos):
            vis[pt]=1
            pt=abs(pt-bs[pt])
    if(f==1 or pt==pos):
        print("true")
    else:
        print("false")