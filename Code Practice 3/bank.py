import pickle
def adddata():
    f=open("bin.dat","ab")
    acno=int(input("Enter A/C number: "))
    name=input("Enter name: ")
    bal=int(input("Enter balance: "))
    rec=[acno,name,bal]
    pickle.dump(rec,f)
    f.close()

def show():
    f=open("bin.dat","rb")
    rec=[]
    while True:
        try:
            rec=pickle.load(f)
            print(rec)
        except:
            break
    f.close()

ch='y'
while ch=='y' or ch=='Y':
    print("1.Add data")
    print("2.Display")
    print("0.Exit")
    n=int(input("Enter choice: "))
    if n==1:
        adddata()
    elif n==2:
        show()
    elif n==3:
        break
    else:
        print("Invalid input")
    ch=input("Do you want to continue(y/n): ")
