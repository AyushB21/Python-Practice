def pushdata(stack):
    student=[]
    rollno=int(input("Enter roll no: "))
    name=input("Enter name: ")
    student=[rollno,name]
    stack.append(student)
def popdata(stack):
    if len(stack)==0:
        print("Empty stack")
    else:
        print(stack.pop())
        print("Element removed")
def showdata(stack):
    if len(stack)==0:
        print("Empty stack")
    else:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
'''If dict and ant to display only name then
print(stack[i]['name']'''
