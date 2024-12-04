f=open("abc.txt")
f1=open("lmn.txt","w")
l=f.read()
print(l)
for i in range(len(l)):
    if l[i].isspace():
        if l[i+1].isspace()==False:
            f1.write(l[i])
    else:
        f1.write(l[i])
            
f.close()
f1.close()
