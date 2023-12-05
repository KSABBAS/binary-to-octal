def prog():
    binary=list(input("enter the binary number : "))
    rt=[]
    p=[]
    n=[]
    rr=[]
    j=0
    t=0
    k=0
    m=0
    cc=0
    b=0
    c=-1
    for i in binary:
        m+=1
    while m!=0:
        rt.append(binary[c])
        c-=1
        m-=1
    binary=rt
    for i in binary:
        n.append(i)
        j+=1
        if (j%3)==0:
            p.append(n)
            n=[]
    for i in n :
        t+=1
    if t!=0:
        if (t<2)and (t>=1):
            n.append(0)
            n.append(0)
            p.append(n)
        if (t<3)and (t>=2):
            n.append(0)
            p.append(n)
    for g in p:
        for i in g:
            g.remove(i)
            i=int(i)
            g.insert(b,i)
            b+=1
        b=0
    for i in p:
        f=i[2]
        h=i[0]
        i[0]=f
        i[2]=h
    for i in p:
        cc+=1
    while cc!=0:
        i=p[cc-1]
        x=(pow(2,2)*i[0])+(pow(2,1)*i[1])+(pow(2,0)*i[2])
        rr.append(str(x))
        cc-=1
    print("the number in octal = "+''.join(rr)+"\n\n")
    agin =input ("wanna do it agin (yes \ no) : ")
    if agin =="yes":
        prog()
prog()