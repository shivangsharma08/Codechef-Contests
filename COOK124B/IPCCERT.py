n,m,k=map(int,input().split())
c=0
for _ in range(n):
    s=0
    ar=[int(i) for i in input().strip().split()]
    s+=(sum(ar)-ar[-1])
    if(s>=m and ar[-1]<=10):
        c+=1
print(c)