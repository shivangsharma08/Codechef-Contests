t=int(input())
while(t):
    n=int(input())
    b=input()
    ar=[int(i) for i in b]
    res=((120-ar.count(0))/120)*100
    if(int(res)>=75):
        print("YES")
    else:
        print("NO")
    t-=1