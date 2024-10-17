class Demo:
    a=0
    b=0
    c=0
    def __init__(self,A,B,C):
        self.a=A
        self.b=B
        self.c=C
    def disp(self):
        print(self.a,self.b,self.c)

class NewDemo(Demo):
    d=0
    def __init__(self,A,B,C,D):
        self.d=D
        super().__init__(A,B,C)
    def disp(self):
        print(self.a,self.b,self.c,self.c)

b1=Demo(100,200,300)
print("BASE CLASS: ")
b1.disp()
c1=NewDemo(10,20,30,40)
print("DERIVED CLASS: ")
c1.disp()
