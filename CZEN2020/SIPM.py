t=int(input())
while(t):
    n=int(input())
    ar=[int(i) for i in input().strip().split()]
    out=list(set(ar))
    pos=neg=0
    for i in range(len(out)):
        if(out[i]>0):
            pos+=out[i]
        else:
            neg+=out[i]
    print(pos,neg)
    t=t-1