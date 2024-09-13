import array as arr
Arr=arr.array('i',[8,2,0,4,7,3,1,6])

#Traversing the array
for x in Arr:
    print(x,end=' ')

#Accessing element at index 5
print("\n Elemet at index 5: ",Arr[5])

#Inserting new element at index 3
Arr.insert(3,10)
print("Array after insertion:")
for x in Arr:
    print(x,end=' ')

#deleting the value 10 from array
Arr.remove(10)
print("\n Array after deletion is :")
for x in Arr:
    print(x, end=' ')

#Searching arrray if value 1 present in it
print("\n 1 is present in array at index: ")
print(Arr.index(1))

#Updating value at index 4 in array
Arr[4]=10
print("The array after updation is: ")
for x in Arr:
    print(x,end=' ')
