f=open("abc.txt","r")
while True:
    str=f.readline()
    if str==" ":
        break
    else:
        print(str)
f.close()

