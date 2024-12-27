n1=float(input("Enter a number: "))
new=round(n1,2)
print(str(n1)+" round to 2 decimal places is ",new)

n2=int(input("Enter number: "))
print("The absolute value of "+str(n2)+" is "+str(abs(n2)))

n3=float(input("Enter a number: "))
n4=float(input("Enter another number: "))
dif=n3-n4
if dif==round(dif):
    print("True")
else:
    print("False")
