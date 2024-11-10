import array
a=array.array('i',[])
n=int(input("Enter number: "))
for i in range(2,n):
    x=0
    if n%i==0:
        for j in range(1,i+1):
            if i%j==0:
                x=x+1
        if x==2:
            a.append(i)
for num in a:
    print(num)
        
    
