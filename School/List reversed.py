li=[17,24,32,47,53]
n=len(li)
for i in range(n-1,-1,-1):
    li.append(li[i])
del li[:n]
print(li)
    
