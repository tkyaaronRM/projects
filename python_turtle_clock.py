import turtle
t = turtle.Turtle()

SHAPE = input('What do you want the shape to be? ')
COLOR = input('What colour do you want it to be? ')

t.shape(SHAPE)
t.color(COLOR)

for i in range(12):
    t.penup()
    t.forward(100)
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(30)
    t.stamp()
    t.backward(140)
    t.left(30)

turtle.mainloop()
