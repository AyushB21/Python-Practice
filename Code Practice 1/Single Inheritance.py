class A:
    i=0
    j=0
    def showij(self):
        print("i=",self.i," j=",self.j)

class B(A):
    k=0
    def showijk(self):
        print(self.i,self.j,self.k)
    def sum(self):
        print("i+j+k=",self.i+self.j+self.k)

ob1=A()
ob2=B()
ob1.i=100
ob1.j=200
print("Content of ob1:")
ob1.showij()
ob2.i=100
ob2.j=200
ob2.k=300
print("Content of Ob2:")
ob2.showijk()
ob2.sum()
