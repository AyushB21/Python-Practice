li=[54,2,34,12,65,87,3,98,13]
n=len(li)
for i in range(n):
    for j in range(i+1,n):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
    print(li)
