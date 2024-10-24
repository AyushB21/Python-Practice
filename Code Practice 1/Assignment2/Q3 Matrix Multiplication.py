a=[[1,2],[3,4]]
b=[[2,0],[1,2]]
r=[[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            r[i][j]+=a[i][k]*b[k][j]

print(r)
