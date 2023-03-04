import turtle

screen = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()

screen.bgcolor('white')
clr = ['red', 'green', 'blue', 'yellow', 'purple']

t1.pensize(4)
t1.penup()
t1.setpos(-120, 30)
t1.backward(200)
t1.left(144)
t1.pendown()
t1.speed(1)

t2.pensize(4)
t2.penup()
t2.setpos(-110, 30)
t2.pendown()

for i in range(5):
    t1.pencolor(clr[i])
    t1.backward(200)
    t1.left(144)
    t2.pencolor(clr[i])
    t2.forward(200)
    t2.right(144)

turtle.done()
