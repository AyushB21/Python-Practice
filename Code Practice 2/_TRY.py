def pr(str):
    print(str)
    return

def prinfo(name,age):
    print("Name:",name)
    print("Age:",age)
    return

def  changelist(li):
    li.append([1,2,3])
    print("Values of function: ",li)
li=[1,2,3]
changelist(li)
print("Changed list: ",li)
print()


def avg1(n1,n2,n3):
    ag=(n1+n2+n3)/3
    print(ag)
    return
