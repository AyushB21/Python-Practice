print('This program display largest number/n')
n=int(input('How many numbers are there: '))
x=int(input('Type the number: '))
m=x
for i in range(1,n):
    x=int(input('Type the number'))
    if (x>m):
        m=x
print(m)

