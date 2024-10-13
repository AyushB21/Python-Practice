class CmpOpr:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        print(self.x)
        print(other.x)
        print('Ob1 < Ob2 : ',end='')
        return self.x<other.x

    def __gt__(self,other):
        print("Ob1 > Ob2 : ",end='')
        return self.x>other.x

    def __le__(self,other):
        print("Ob1 <= Ob2 : ",end='')
        return self.x <= other.x

ob1=CmpOpr(20)
ob2=CmpOpr(30)
print(ob1<ob2)
print(ob1>ob2)
print(ob1<=ob2)
