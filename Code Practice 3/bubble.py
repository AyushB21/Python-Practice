a=[43,6,23,86,92,4]
n=len(a)
for i in range(0,n,1):
    for j in range(0,n-1-i,1):
        if a[j]>=a[j+1]:
            tmp=a[j]
            a[j]=a[j+1]
            a[j+1]=tmp
print(a)
