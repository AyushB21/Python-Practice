def fun(l,n,ele):
    c=0
    for i in l:
        if i==ele:
            c=c+1
    if c>0:
        print("Element found")
    else:
        print("Not Found")
li=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    element=int(input("Enter element: "))
    li.append(element)
ele=int(input("Enter element to search: "))
fun(li,n,ele)
