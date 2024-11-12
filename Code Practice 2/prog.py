import array
a=array.array('i',[10,8,16,42,16,38,24,2,38,11])
n=len(a)
for i in range(0,n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

for i in a:
    print(i,end=' ')
print()

temp=array.array('i',[])
for k in a:
    if k not in temp:
        temp.append(k)
a=temp
for i in a:
    print(i,end=' ')
print()

a=a[::-1]
for i in a:
    print(i,end=' ')
