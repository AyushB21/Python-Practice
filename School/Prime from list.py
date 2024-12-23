def prime(li,size):
    p=0
    for i in li:
        c=0
        for j in range(2,i):
            if i%j==0:
                c=c+1
        if c==0:
            p=p+1
    print("Number of prime values:",p)
l=[13,63,97,2,59,6]
n=len(l)
prime(l,n)
