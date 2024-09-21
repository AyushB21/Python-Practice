class Demo:
    result=0
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

d=Demo()
d.add(1,2)      #It will give error because add function defined later will be considered by python
