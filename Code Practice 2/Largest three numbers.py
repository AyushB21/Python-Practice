n=int(input("Enter how many numbers: "))
b1=0
b2=0
b3=0
for i in range(n):
    a=int(input("Enter number: "))
    if a>b1:
        b1,b2,b3=a,b1,b2
    elif a>b2:
        b2,b3=a,b2
    elif a>b3:
        b3=a

print("biggest three numbers are: ",b1,b2,b3)
