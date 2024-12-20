def fun():
    x=int(input("Enter x: "))
    n=int(input("Enter n: "))
    s=0
    for i in range(1,n+1):
        num=x**i
        f=1
        for j in range(1,i+1):
            f=f*j
        k=num/f
        s=s+k
    print(s)
        
