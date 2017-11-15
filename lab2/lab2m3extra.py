def ok():
    import random
    a = []
    b = []
    for i in range(11):
        i = random.randint(1,50)
        a.append(i)
    for i in range(11):
        i = random.randint(1,50)
        b.append(i)
    c = []
    for i in a:
        for h in b:
            if (i == h):
                c.append(i)
    print(a)
    print(b)
    print(c)

##one line
ok()
##one line
