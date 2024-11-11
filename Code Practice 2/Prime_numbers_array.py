import array
a=array.array('i',[])
n=int(input("Enter the number till which prime numbers to be printed: "))
for i in range(n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        a.append(i)
for x in a:
    print(x,end=' ')
