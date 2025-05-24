import turtle

t = turtle.Turtle()
t.speed(0)

def hexagon():
    for i in range(6):
        t.forward(30)
        t.left(60)

t.color('purple')
for i in range(18):
    hexagon()
    t.left(20)

t.right(90)
t.penup()
t.forward(50)
t.pendown()

t.color('green')
t.begin_fill()
t.right(90)
t.forward(5)
t.left(90)
t.forward(100)
t.left(90)
t.forward(10)
t.left(90)
t.forward(100)
t.left(90)
t.forward(5)
t.end_fill()

def teleport(x, y):
    t.goto(x, y)

def moveForward():
    t.forward(20)

def moveBackward():
    t.backward(20)

def turnLeft():
    t.left(90)

def turnRight():
    t.right(90)

def stylusUp():
    t.penup()

def stylusDown():
    t.pendown()

def drawCircle(radius):
    t.circle(radius)

def drawTriangle(length):
    for i in range(3):
        t.forward(length)
        t.left(120)

def stylusR():
    t.color('red')

def stylusG():
    t.color('green')

def stylusY():
    t.color('yellow')

def stylusB():
    t.color('blue')

def stylusW():
    t.color('white')

def stylusBk():
    t.color('black')

def stylusP():
    t.color('purple')

t.speed(2)
turtle.listen()

turtle.onkey(moveForward, 'w')
turtle.onkey(turnLeft, 'a')
turtle.onkey(moveBackward, 's')
turtle.onkey(turnRight, 'd')

turtle.onkey(stylusUp, 'z')
turtle.onkey(stylusDown, 'x')

turtle.onkey(stylusR, 'r')
turtle.onkey(stylusG, 'g')
turtle.onkey(stylusY, 'y')
turtle.onkey(stylusB, 'b')
turtle.onkey(stylusW, '1')
turtle.onkey(stylusBk, '2')

turtle.onscreenclick(teleport, 1)

turtle.mainloop()
