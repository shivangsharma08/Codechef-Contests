def const(let):
    ar=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W', 'X','Y','Z']
    c=[]
    for i in range(len(let)):
        if(let[i] in ar):
            c.append(let[i])
    if(len(set(c))>=5):
        return True
    else:
        return False
def vow(let): 
    return ((let == 'A') or (let == 'E') or 
            (let == 'I') or (let == 'O') or 
            (let == 'U'))
def isConsec(s):
    vc = 0
    for x in s:
        if vow(x):
            vc += 1
            if(vc>=3): 
                return True
        else:
            vc=0
    return False
s=input()
if(isConsec(s) and const(s)):
    print("GOOD")
else:
    print(-1)