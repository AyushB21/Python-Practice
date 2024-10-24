n=int(input("Enter n: "))
c=0
i=2
while c<n:
    chk=0
    for j in range(1,i+1):
        if i%j==0:
            chk+=1
    if chk==2:
        print(i)
        c+=1
    i+=1
