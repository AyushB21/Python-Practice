def indata(student):
    rno=int(input("Enter roll: "))
    name=input("Enter name: ")
    temp=[rno,name]
    student.append(temp)
def deldata(student):
    if len(student)==0:
        print("Empty!!")
    else:
        temp=student.pop(0)
        print("Removed",temp)
def showdata(student):
    if len(student)==0:
        print("EMPTY")
    else:
        for rec in student:
            print(rec)
student=[]
