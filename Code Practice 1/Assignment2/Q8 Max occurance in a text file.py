f=open("read.txt","r")
st=f.read()
li=st.split()
print(li)
c=0
for i in li:
    counter=li.count(i)
    if counter>c:
        c=counter

for j in li:
    if li.count(j)==c:
        print("Most occuring word: ",j)
        print(c,"times")
        break

f.close()
