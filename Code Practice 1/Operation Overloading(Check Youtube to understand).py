class OprOverloadingDemo:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):
        print("Value of obj1 = ",self.x)
        print("Value of obj2 = ",other.x)
        print("Addition: ",end='')
        return ((self.x+other.x))

ob1=OprOverloadingDemo(20)
ob2=OprOverloadingDemo(30)
ob3=ob1+ob2
print(ob3)
