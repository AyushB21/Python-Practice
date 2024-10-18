Lst=[]
n=int(input("Enter number of elements in list: "))
for i in range(n):
    ele=eval(input("Enter element: "))
    Lst.append(ele)

print(Lst)

temp=[]
for i in Lst:
    if i not in temp:
        temp.append(i)

for x in temp:
    c=0
    for occurance in Lst:
        if x==occurance:
            c=c+1
    if c==1:
        print(x,"occurs",c,"time.")
    else:
        print(x,"occurs",c,"times.")
