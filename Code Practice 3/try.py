a=input("Enter a string: ")
st=""
for i in a:
    print(i)
    st=a+st
print(st)
if st==a:
    print("Pallindrome: ")
else:
    print("Not a pallindrome")
