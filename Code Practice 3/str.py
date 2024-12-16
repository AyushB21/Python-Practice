a=input("Enter: ")
c=0
for i in a:
    if not(i.isalpha() or i.isnumeric()):
        c=c+1
print(c)
