li=[]
n=int(input("Enter number of elements in list: "))
for i in range(n):
    ele=eval(input("Enter element: "))
    li.append(ele)

print("Elements before sorting: ",li)

#Code till here to take inputs

li1=[]      #List with elements as strings
lenli=[]    #List with length of each elements of li1
for j in li:
    element=str(j)
    li1.append(element)
    lenli.append(len(element))

n=len(lenli)
final=[]    #Final sorted list
for k in range(n):      #We iterate through the length of list
    sm=min(lenli)
    element_index=lenli.index(sm)       #Here we find index of smallest element of lenli 
    lenli.pop(element_index)            #Remove smallest element so next time next smallest
    final.append(li.pop(element_index))

print()
print("Elements after sorting: ",final)
