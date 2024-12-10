n=int(input("Enter how many admission no. you have to give: "))
d={}

for l in range (n):
    v=()
    k=int(input("Enter admission no. of child..."))
    for q in range (2):
        if q==0:
            x=input("Enter name of child.....")
        elif q==1:
            x=input("Enter class of child...")
        v+=(x,)
        d[k]=v
    del v
c=0
while (c!=5):
    c=int(input("""Enter
1 for Add
2 for Remove
3 for Search
4 for Display
5 for Exit
"""))

    if c==1:
        n+=1
        for a in range (n-1,n):
            v=()
            k=int(input("Enter admission no. of child..."))
            for e in range (2):
                if e==0:
                    x=input("Enter name of child.....")
                else:
                    x=input("Enter class of child...")
                v+=(x,)
            d[k]=v
    elif c==2:
        r=int(input("Enter admission no. of child..."))
        if r in d:
            del d[r]
        else:
            print("Element Not Found!!")
    elif c==3:
        s=int(input("Enter admission no. of child..."))
        if s in d:
            print("Element Found")
        else:
            print("Element Not Found!!")
    elif c==4:
        print(d)
    elif c==5:
        pass
    else:
        print("Enter no. given in list")
