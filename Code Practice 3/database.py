d={}
def add():
    adm=int(input("Enter Admission No.: "))
    name=input("Enter Name: ")
    cls=input("Enter class: ")
    sec=input("Enter section: ")
    roll=int(input("Enter roll no.: "))
    d[adm]=(name,cls,sec,roll)
def remove():
    adm=int(input("Enter Admission No.: "))
    if adm in d:
        del d[adm]
    else:
        print("Student not found!!")
def search():
    adm=int(input("Enter admission no. to search: "))
    if adm in d:
        print(d[adm])
    else:
        print("Student not found")
b=1
while b==1:
    print("1.Add student")
    print("2.Remove student")
    print("3.Search student")
    print("4.Display")
    print("5.Exit")
    n=int(input("Enter your choice: "))
    if n==1:
        add()
    elif n==2:
        remove()
    elif n==3:
        search()
    elif n==4:
        print(d)
    elif n==5:
        b=2
    else:
        print("Wrong value")
