import array
a=array.array('i',[])
n=int(input("Enter number: "))
while n>2:
    while n%2==0:
        a.append(2)
        n=n//2

    for i in range(3,int(n)+1,2):
        x=0
        if n%i==0:
            for j in range(1,i+1):
                if i%j==0:
                    x=x+1
            if x==2:
                a.append(i)
            n=n//i
            
            
        
for num in a:
    print(num)
        
    
