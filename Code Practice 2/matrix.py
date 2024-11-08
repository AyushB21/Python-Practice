a=[[1,1],[1,1]]
b=[[2,2],[2,2]]
c=[[0,0],[0,0]]
for i in range(len(a)):     # XXX==>len(a)
    for j in range(len(b[0])):  #YYY==>len(b[0])
        for k in range(len(b)):     #ZZZ==>len(b)
            c[i][j]=c[i][j]+a[i][k]*b[k][j]
for i in c: 
    print(i) 
