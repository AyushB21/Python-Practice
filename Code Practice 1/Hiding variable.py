class Prac:
    x=5
    def disp(self,x):
        
        print("Local Variable x is: ",x)
        print("Instance variable of x is: ",self.x)

obj=Prac()
obj.disp(50)
