import array
sum1=0
a=array.array('i',[1,2,3,4])
for i in a:
    sum1=sum1+i
print(sum1)

a.insert(4,5)
for i in a:
    print(i)
