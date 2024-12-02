def cal():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("1 to add")
    print("2 to subtract")
    print("3 to multiply")
    print("4 to divide")
    print("5 to find modulos")
    print("6 to raise first number by second")
    c=int(input("Enter your Choice: "))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()
    elif c==4:
        div()
    elif c==5:
        mod()
    elif c==6:
        powe()
def add():
    f=a+b
    print(f)
def sub():
    f=a-b
    print(f)
def mul():
    f=a*b
    print(f)
def div():
    f=a/b
    print(f)
def mod():
    f=a%b
    print(f)
def powe():
    f=a**b
    print(f)

cal()
y=input("Do you want to run program again? Y for yes and N for no")
if y=="Y":
    cal()

    
