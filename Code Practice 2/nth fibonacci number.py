import array
ar=array.array('i',[0,1])
a,b=0,1
c=0
count=0
n=int(input("Enter nth number to find: "))
while True:
    c=a+b
    ar.append(c)
    a,b=b,c
    count+=1
    if count==n:
        break
print(ar[n-1]) 
