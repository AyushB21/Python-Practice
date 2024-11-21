print("Equation: ax^2+bx+c=0")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=(b*b)-(4*a*c)
r1=(-(b)+d**(1/2))/2*a
r2=(-(b)-d**(1/2))/2*a
print("Two roots are: ",r1, r2)
