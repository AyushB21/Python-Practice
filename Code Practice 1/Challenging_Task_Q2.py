def fun():
    n=int(input())
    if n<1 or n>10e5:
        return "n out of constraint"
    li=[]
    for i in range(n):
        data=int(input())
        if data<1 or data>10e9:
            return "Data out of constraint"
        li.append(data)     #Adding data in a list
    v=[]
    to_add=0    #Value to be added to each term
    for i in li:
        disp=i+to_add
        n=0
        while True:
            value=2**n
            if value>disp:  #Finding 2^power that is greater
                break
            else:
                n+=1
        f=2**(n-1)  #Taking 2^power less than the data so (n-1)
        v.append(f)
        to_add=disp-f

    return(max(v))

        
        
            

