def mul(x,y): 
    if x < y: 
        return mul(y, x) 
    elif y != 0: 
        return (x + mul(x, y - 1)) 
    else: 
        return 0
a=int(input())
b=int(input())
res=mul(a,b)
print(res)