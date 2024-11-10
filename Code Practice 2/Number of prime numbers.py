import array
a=array.array('i',[])
n=int(input("Enter number of prime numbers: "))
c=0
i=1
while c!=n:
    x=0
    for j in range(1,i+1):
        if i%j==0:
            x=x+1
    if x==2:
        c=c+1
        a.append(i)
    i=i+1

for prime in a:
    print(prime)
