a=[1,2,3,4,5]
b=[6,7,8,9,0]
n=len(a)
for i in range(n):
    a[i],b[i]=b[i],a[i]
print(a)
print(b)
