t=int(input())
while(t):
    n=int(input())
    s=input()
    ar=[chr(i) for i in range(97,113)]
    ar2=ar
    res=[int(i) for i in s]
    out=""
    for i in range(len(res)):
        if(res[i]==1):
            ar=ar[len(ar)//2 : len(ar)]
        elif(res[i]==0):
            ar=ar[:len(ar)//2]
        if((i+1)&3==0):
            out+=ar[0]
            ar=ar2
    print(out)
    t-=1