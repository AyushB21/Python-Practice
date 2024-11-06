import array
a=array.array('i',[])
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
a.append(n1)
a.append(n2)
for i in range(1,a[0]+1):
    if a[0]%i==0 and a[1]%i==0:
        gcd=i

print(gcd)
