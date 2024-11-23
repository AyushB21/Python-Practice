import array
a=array.array('i',[])
n=int(input("Enter number : "))
for i in range(2,n):
    if n%i==0:
        a.append(i)

print(a[0])
        
