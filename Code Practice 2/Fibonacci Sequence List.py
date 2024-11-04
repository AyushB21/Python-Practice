n=int(input("Enter n: "))
a=0
b=1
li=[a,b]
for i in range(1,n-1):
    c=a+b
    li.append(c)
    a=b
    b=c

for i in li:
    print(i,end=' ')
