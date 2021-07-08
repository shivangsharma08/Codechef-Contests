t=int(input())
while(t):
    n,k,x,y=map(int,input().split())
    cy=f=0
    while(cy<=n):
        x=(x+k)%n
        if(x==y):
            f=1
        cy+=1
    print("YES" if f==1 else "NO")
    t=t-1