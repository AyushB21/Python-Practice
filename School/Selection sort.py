a=[51,23,1,43,59]
n=len(a)
for i in range(0,n,1):
    small=a[i]
    pos=i
    for j in range(i+1,n):
        if a[j]<small:  ##For descending change sign to >##
            small=a[j]
            pos=j
        tmp=a[i]
        a[i]=a[pos]
        a[pos]=tmp
    print(a)
        
