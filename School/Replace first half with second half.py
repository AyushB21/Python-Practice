a=[1,2,3,4,5]
n=len(a)
mid=n//2
for i in range(mid):
    if (mid+i+1)<n:
        a[i],a[mid+i+1]=a[mid+i+1],a[i]
print(a)
