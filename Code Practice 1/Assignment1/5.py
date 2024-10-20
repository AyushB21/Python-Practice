Lst=[]
n=int(input("Enter number of elements in list: "))
for i in range(n):
    ele=eval(input("Enter element: "))
    Lst.append(ele)

print(Lst)

new=[]

for j in Lst:
    c=0
    for p in range(1,j+1):
        if j%p==0:
            c=c+1
    if c==2:
        new.append(True)
    else:
        new.append(False)
        
print(new)
