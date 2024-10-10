a=0
b=1
print(a,end=' ')
print(b,end=' ')
for i in range(10):
    if b==8:
        break
    c=a+b
    a=b
    b=c
    print(c, end=' ')
    
    
