class A():
    name=" "
    age=0

class B(A):
    height=" "

class C(B):
    weight=" "
    def Read(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter age: "))
        self.height=input("Enter height: ")
        self.weight=int(input("Enter weight: "))
    def disp(self):
        print(self.name,self.age,self.height,self.weight,sep='\n')

obj=C()
obj.Read()
obj.disp()
