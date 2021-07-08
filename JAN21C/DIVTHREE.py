t=int(input())
while(t):
    n,k,d=map(int,input().split())
    ar=[int(i) for i in input().split()]
    if(sum(ar)<k):
        print(0)
    else:
        if((sum(ar)//k) > d):
            print(d)
        else:
            print(sum(ar)//k)
    t-=1