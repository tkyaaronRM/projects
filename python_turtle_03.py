import turtle, os
john = turtle.Turtle()

# Python Turtle code here:

john.pensize(3)

def teleport(x, y):
    john.goto(x, y)

def moveForward():
    john.forward(20)

def moveBackward():
    john.backward(20)

def turnLeft():
    john.left(90)

def turnRight():
    john.right(90)

def stylusUp():
    john.penup()

def stylusDown():
    john.pendown()

def drawCircle(radius):
    john.circle(radius)

def drawTriangle(length):
    for i in range(3):
        john.forward(length)
        john.left(120)

def stylusR():
    john.color('red')

def stylusG():
    john.color('green')

def stylusY():
    john.color('yellow')

def stylusB():
    john.color('blue')

def stylusW():
    john.color('white')

def stylusBk():
    john.color('black')

    
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

while True:
    os.system('cls')
    print('---------------------')
    print('Python Turtle Drawing')
    print('---------------------')
    print('1. Create Shapes')
    print('2. Clear Canvas')
    print('---------------------')
    print()
    print('Choice your option (1 to 2)')
    choice = input('> ')

    if choice == '1':
        os.system('cls')
        print('Choose your shape (1 or 2)')
        print('1. Circle')
        print('2. Triangle')
        print('--------------------------')
        shape = input('> ')

        if shape = '1':
            os.system('cls')
            radius = input('Radius of circle: ')
            drawCircle(radius)

        if shape = '2':
            os.system('cls')
            length = input('Length of each side of triangle: ')
            drawTriangle(length)
        
    if choice == '2':
        turtle.clear()
        
turtle.mainloop()
