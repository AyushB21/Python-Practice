def remove_first_last(list1):
    n=len(list1)
    new=list1[1:n-1]
    return(new)
    
List1=[]
n=int(input("Enter number of elements in list: "))
for i in range(n):
    ele=eval(input("Enter element: "))
    List1.append(ele)

print(List1)
print(remove_first_last(List1))
