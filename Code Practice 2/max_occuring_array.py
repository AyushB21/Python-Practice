import array
a=array.array('i',[1,2,2,3,3,3,4,5])
maxn=0
for i in a:
    s=a.count(i)
    if s>maxn:
        maxn=s

for i in a:
    s=a.count(i)
    if maxn==s:
        print(i)
        break
