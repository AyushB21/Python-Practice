import array
a=array.array('i',[])
n=int(input("Enter number of terms: "))
for i in range(n):
    ele=int(input("Enter element: "))
    a.append(ele)

temp=[]
for i in a:
    if i not in temp:
        temp.append(i)

temp.sort()
f_array=array.array('i',[])
f_array.fromlist(temp)
a=f_array
for i in a:
    print(i)
        
