n=int(input())
v=input()
ar=[str(x) for x in v]
if(ar.count('V')>ar.count('H')):
    print("Virat")
if(ar.count('H')>ar.count('V')):
    print("Harshit")
if(ar.count('V')==ar.count('H')):
    print("Friendship")