Lst=[]
n=int(input("Enter number of elements in list: "))
for i in range(n):
    ele=eval(input("Enter element: "))
    Lst.append(ele)

print("Original: ",Lst)

new=[]
for i in Lst:
    new.append(i)
    new.append(i)

Lst=new

print("Duplicated: ",Lst)
