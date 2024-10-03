starship="Enterprise"
n=input("Enter string to check if Enterprise starts with it: ")
l=len(n)
if starship[:l]==n:
    print("True")
else:
    print("False")

z=input("Enter string to check if Enterprise ends with it: ")
l=len(z)
if starship[-l:]==z:
    print("True")
else:
    print("False")
