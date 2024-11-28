f=open("new.txt")
rec=f.read()
l=rec.split()
for i in l:
    if i[0]=="s" or i[0]=="S":
        print(i[::-1],end=' ')
    else:
        print(i,end=' ')
        

f.close()

        
