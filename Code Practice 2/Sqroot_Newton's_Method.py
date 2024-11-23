x=int(input("Enter number: "))
n=x
for i in range(10):
    j=0.5*(n+(x/n))
    n=j

print(n)

