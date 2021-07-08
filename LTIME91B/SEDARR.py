t=int(input())
while(t):
    n,k=map(int,input().split())
    ar=[int(i) for i in input().strip().split()]
    s=sum(ar)
    c=0
    if(s%k==0):
        c=0
    else:
        s+=(s%k)
        c+=1
    print(c)
    t-=1