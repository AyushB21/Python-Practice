class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def Display(self):
        print("X coordinate: ",self.x)
        print("Y coordinate: ",self.y)
    def Translate(self):
        self.x+=self.x
        self.y+=self.y

x=int(input("Enter x: "))
y=int(input("Enter y: "))
obj=Point(x,y)
obj.Display()
obj.Translate()
print("Translated to: ")
obj.Display()
