binary=str(input("Enter binary: "))         #'111001'
l=list(binary)
n=len(l)-1
dec=0
for i in l:
    dec+=int(i)*(2**n)
    n=n-1

print("Decimal of",binary,"is: ",dec)
