n1=int(input("Enter First number: "))
n2=int(input("Enter second number: "))
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
c=int(input("Enter choice: "))
if c==1:
    print(n1,"+",n2,"=",n1+n2)
elif c==2:
    print(n1,"i",n2,"=",n1-n2)
elif c==3:
    print(n1,"*",n2,"=",n1*n2)
elif c==4:
    print(n1,"/",n2,"=",n1/n2)
else:
    print("Choice out of range")
