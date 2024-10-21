def Extract_Even(List):
    new=[]
    for i in List:
        if i%2==0:
            new.append(i)
    return new

List1=[]
n=int(input("Enter number of elements in list: "))
for i in range(n):
    ele=eval(input("Enter element: "))
    List1.append(ele)

print(List1)

print(Extract_Even(List1))
