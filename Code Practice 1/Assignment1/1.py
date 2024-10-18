def Replicate_n_times(Lst,n):
    new=[]
    for i in Lst:
        for j in range(n):
            new.append(i)
    Lst=new
    print(Lst)
