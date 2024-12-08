li=[]
n=int(input("Enter number of elements in list: "))
for i in range(n):
    e=int(input("Enter the element: "))
    li.append(e)
for i in range(n):
    temp=li[i]
    j=i-1
    while(li[j]>temp and j>=0):
        li[j+1]=li[j]
        j-=1
    li[j+1]=temp
print(li)
