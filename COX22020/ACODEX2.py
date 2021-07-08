n=int(input())
c=0
for _ in range(n):
    ar=list(map(int,input().strip().split()))
    if(ar.count(1)>=2):
        c+=1
print(c)