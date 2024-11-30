n=int(input('How many terms are there: '))
c1=0
c2=0
c3=0
for i in range(n):
    if (i<n):
        x=int(input('Type the nuber: '))
        if (x<=15):
            c1=c1+1
        elif (x<=30):
            c2=c2+1
        elif (x>30):
            c3=c3+1
print(c1,c2,c3)
