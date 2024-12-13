f=open("abc.txt","r")
str=f.read()
li=str.split()
for i in li:
    if i[0]=='I' or i[0]=='i':
        print(i[::-1],end=' ')
    else:
        print(i,end=' ')
