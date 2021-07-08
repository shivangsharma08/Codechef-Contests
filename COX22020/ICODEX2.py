n=int(input())
phole=input()
Ds=Us=c=0
ar=[str(i) for i in phole]
for i in range(len(ar)):
    if(ar[i]=='D'):
        Ds+=1
    elif(ar[i]=='U'):
        Us+=1
        if(Ds==Us):
            c+=1
            Ds=0
            Us=0
print(c)