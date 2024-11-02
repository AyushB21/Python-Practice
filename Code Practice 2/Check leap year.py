n=int(input("Enter year: "))
c=0
for i in range(n,n+50):
    if c<10:
        if i%4==0:
            if i%100==0:
                if i%400!=0:
                    print(i,end=' ')
                    c=c+1
            else:
                print(i,end=' ')
                c=c+1
    else:
        break
                
    
