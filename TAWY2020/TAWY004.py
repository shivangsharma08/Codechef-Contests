def leftRotate(arr, d, n): 
    d = d % n 
    g_c_d = gcd(d, n) 
    for i in range(g_c_d): 
        temp = arr[i] 
        j = i 
        while 1: 
            k = j + d 
            if k >= n: 
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k] 
            j = k 
        arr[j] = temp 
def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a % b) 
N,n,x=map(int,input().split())
ar=[int(i) for i in range(1,N+1)]
leftRotate(ar,n,N) 
for i in range(len(ar)):
    if(ar[i]==x):
        print(i+1)
        break