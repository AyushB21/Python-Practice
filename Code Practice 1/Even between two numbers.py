a=int(input("Enter a: "))
b=int(input("Enter b: "))
li=[]
for i in range(a,b):
    if i%2==0:
        li.append(i)
print(li)
