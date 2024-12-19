import turtle
turtle.shape("turtle")
turtle.write("Home = ", True, align="center")
turtle.write((0,0), True)

t = turtle.Pen()

t.left(90)
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(115)
turtle.speed(10)
