def remove_negative(Lst):
    newLst=[]
    for i in Lst:
        if i>=0:
            newLst.append(i)
    Lst=newLst
    return Lst
