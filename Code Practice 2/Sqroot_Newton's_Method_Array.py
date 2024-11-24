import array
a=array.array('i',[])
x=int(input("Enter number: "))
a.append(x)
n=x
a.append(x)
for i in range(10):
    j=0.5*(a[1]+(a[0]/a[1]))
    a[1]=j

print(a[1])
