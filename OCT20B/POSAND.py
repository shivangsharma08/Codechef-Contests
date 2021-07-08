def two(n):
    x=n
    y=not(n&(n-1))
    return x and y
t=int(input())
while(t):
    i=0
    n=int(input())
    if(n==1):
        print(1)
    elif(n==3):
        print(1,3,2)
    elif(n==5):
        print(2,3,1,5,4)
    elif(two(n)):
        print(-1)
    else:
        print(2,3,1,5,4,end=" ")
        i=6
        while(i<=n):
            if(two(i)):
                print(i+1,i,end=" ")
                i+=2
            else:
                print(i,end=" ")
                i+=1;
        print("\n")
    t=t-1