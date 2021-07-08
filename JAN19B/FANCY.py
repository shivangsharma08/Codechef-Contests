for _ in range(int(raw_input())):
    f=0
    s=raw_input()
    s=s.split()
    for i in s:
        if i=="not":
            f=1
    if f==1:
        print "Real Fancy"
    else:
        print "regularly fancy"