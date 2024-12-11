l=[]
n=int(input("Enter number of elements in list: "))
c=0
for i in range(n):
    e=int(input("Enter the element: "))
    l.append(e)
search=int(input("Enter element to search: "))
for i in l:
    if i==search:
        c=c+1
if c>0:
    print("FOUND")
else:
    print("NOT FOUND")
