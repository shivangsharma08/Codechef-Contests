from collections import defaultdict
t=int(raw_input())
for _ in range(t):
    l=[]
    n,m=map(int,raw_input().split())
    fruit=[int(i) for i in raw_input().split()]
    price=[int(i) for i in raw_input().split()]
    d=defaultdict(list)
    x=zip(fruit,price)
    for ftype,prc in x:
        d[ftype].append(prc)
    d1=dict(d)
    val=d1.values()
    for i in range(len(d1)):
        l.append(sum(val[i]))
    print min(l)