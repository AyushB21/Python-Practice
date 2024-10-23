class Circle():
    def __init__(self):
        self.r=10   #Radius
    def get_radius(self):
        print("Radius is: ",self.r)
    def calc_area(self):
        ar=3.14*self.r*self.r
        print("Area is: ",ar)

class Cylinder(Circle):
    def __init__(self,height):
        self.h=height
        super().__init__()
    def Calc_Area(self):
        print("Area of Cylinder:")
        ar=2*3.14*self.r*self.r+(2*3.14*self.r*self.h)
        print(ar)

h=int(input("Enter height of cylinder: "))
obj=Cylinder(h)
obj.get_radius()
obj.calc_area()     #Area of Circle
obj.Calc_Area()     #Surface Area of Cylinder

