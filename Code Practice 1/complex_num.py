class comp():
    a1=0
    b1=0
    a2=0
    b2=0
    def add(self):
        c1=complex(self.a1,self.b1)
        c2=complex(self.a2,self.b2)
        print("Sum of given complex number is:")
        print(c1+c2)
    def subt(self):
        c1=complex(self.a1,self.b1)
        c2=complex(self.a2,self.b2)
        print("Subtracting:")
        print(c1-c2)
    def mult(self):
        c1=complex(self.a1,self.b1)
        c2=complex(self.a2,self.b2)
        print("Multiplication:")
        print(c1*c2)
    def divi(self):
        c1=complex(self.a1,self.b1)
        c2=complex(self.a2,self.b2)
        print("Dividing:")
        print(c1/c2)
    def chkeq(self):
        c1=complex(self.a1,self.b1)
        c2=complex(self.a2,self.b2)
        if c1==c2:
            print(c1,"=",c2,":TRUE") 
    def chkgr(self):
        c1=complex(self.a1,self.b1)
        c2=complex(self.a2,self.b2)
        modc1=((self.a1**2)+(self.b1**2))**0.5
        modc2=((self.a2**2)+(self.b2**2))*0.5
        if modc1>=modc2:
            print(c1,">=",c2,"= True")
        else:
            print(c1,">=",c2,"= False")
    def chksm(self):
        c1=complex(self.a1,self.b1)
        c2=complex(self.a2,self.b2)
        modc1=((self.a1**2)+(self.b1**2))**0.5
        modc2=((self.a2**2)+(self.b2**2))*0.5
        if modc1<=modc2:
            print(c1,"<=",c2,"= True")
        else:
            print(c1,"<=",c2,"= False")
        
    
        
ob=comp()
ob.a1=int(input("Enter a1: "))
ob.b1=int(input("Enter b1: "))
ob.a2=int(input("Enter a2: "))
ob.b2=int(input("Enter b2: "))
ob.add()
ob.subt()
ob.mult()
ob.divi()
ob.chkeq()
ob.chkgr()
ob.chksm()
