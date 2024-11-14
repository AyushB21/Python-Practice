a=int(input("Enter start number: "))
b=int(input("Enter stop number: "))
for i in range(a,b+1):
    c=0
    for x in range(1,i+1):
        if (i%x==0):
            c=c+1
    if (c==2):
        print(i, end=' ')
    
