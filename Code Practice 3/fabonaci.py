a=0
b=1
li=[]
li.append(a)
li.append(b)
c=0
while True:
    if c>4000000:
        break
    c=a+b
    li.append(c)
    a=b
    b=c
s=0
for j in li:
    if j%2==0:
        s=s+j
print(s)
