li=[1,2,3,4,5]
n=len(li)
for i in range(0,n-1,2):
    li[i],li[i+1]=li[i+1],li[i]
print(li)
    
