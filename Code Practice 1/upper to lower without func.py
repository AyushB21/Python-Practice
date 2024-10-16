n=input("Enter string in upper case: ")
c=0
for i in n:
    if i.isalpha():
        x=ord(i)
        x=x+32
        print(chr(x),end='')
    else:
        print(i,end='')
    c=c+1
print()
print("Length: ",c)
