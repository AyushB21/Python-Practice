num=7
x=num
for i in range(1,6,1):
    num=num-1
    for j in range(1,num):
        print("*",end=" ")
        x=num-1
    print()
