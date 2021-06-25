def generator(length):
    import random
    password=""
    for i in range(length):
        g=random.randint(1,4)
        if g==1:
            l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            a=random.randint(0,len(l)-1)
            b=l[a]
            password=password+b
        if g==2:
            a=random.randint(0,9)
            b=str(a)
            password=password+b
        if g==3:
            l=["?","*","%","#","@","^"]
            a=random.randint(0,len(l)-1)
            b=l[a]
            password=password+b
        if g==4:
            l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            a=random.randint(0,len(l)-1)
            b=l[a]
            b=b.upper()
            password=password+b        
    g="?*%#@^"
    chk=1
    for i in g:
        if i in password:
            chk=0
            break
    if chk==1:
        a=random.randint(0,len(g)-1)
        b=g[a]
        password=password+b
    else:
        pass
    chk=1
    g="0123456789"
    for i in g:
        if i in password:
            chk=0
            break
    if chk==1:
        a=random.randint(0,len(g)-1)
        b=g[a]
        password=password+b
    else:
        pass
    chk=1
    g="abcdefghijklmnopqrstuvwxyz"
    for i in g:
        if i in password:
            chk=0
            break
    if chk==1:
        a=random.randint(0,len(g)-1)
        b=g[a]
        password=password+b
    else:
        pass
    return password
