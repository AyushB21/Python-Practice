x=int(input('Type the number: '))
c=0
for i in range(1,x):
    if (x%i==0):
       c=c+1
if (c==2):
    print('Prime')
else:
    print('Not Prime')
