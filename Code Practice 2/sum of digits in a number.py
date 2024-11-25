n=int(input("Enter number: "))
s=0
while n>0:
    temp=n%10
    s=s+temp
    n=n//10

print(s)
