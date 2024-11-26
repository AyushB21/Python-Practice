n=int(input("How many numbers in the set: "))
so=0
se=0
for i in range(n):
    a=int(input("Enter number: "))
    if (a%2==0):
        se=se+a
    else:
        so=so+a

print("Sum of even numbers: ",se)
print("Sum of odd numbers: ",so)
