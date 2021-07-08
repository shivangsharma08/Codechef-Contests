n=int(input())
ar=list(map(int,input().strip().split()))
ar.sort()
c=tot=0
for i in range(len(ar)):
    tot+=ar[i]
    if(tot<=500):
        c+=1
print(c)