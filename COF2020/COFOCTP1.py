n=int(input())
coins=[int(i) for i in input().strip().split()]
r=[1]
h=[0]
while((sum(r) + sum(h) < sum(coins)) and sum(r) > sum(h)):
    r.append(1)
    h.append(1)
if(sum(r) > sum(h) and (sum(r) + sum(h) == sum(coins))):
    print("YES")
else:
    print("NO")