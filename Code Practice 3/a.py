def funin(x,y):
    global z
    x+=y
    y=y-1
    z*=(x-y)
def funout(y,z):
    global x
    x=x*y
    y=y+1
    z/=(x+y)
x,y,z=20,30,10
funout(z,y)
print(x,y,z,sep='#')
funin(x,y)
print(x,y,z,sep='@')
