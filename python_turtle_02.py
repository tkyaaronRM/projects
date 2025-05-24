import turtle
tuli = turtle.Turtle()

### Pacman
##tuli.color("black", "yellow")
##tuli.pensize(2)
##tuli.begin_fill()
##tuli.right(45)
##tuli.forward(50)
##tuli.right(135)
##tuli.forward(50)
##tuli.left(90)
##
##for i in range(319):
##    tuli.forward(1)
##    tuli.left(1)
##    
##tuli.end_fill()
##tuli.penup()
##tuli.goto(38, -5)
##tuli.color("black")
##tuli.pensize(5)
##tuli.pendown()
##tuli.circle(1)
##tuli.penup()

# Pacman Ghost
tuli.penup()
tuli.goto(-70, 0)
tuli.pendown()
tuli.color("black", "red")
tuli.pensize(2)
tuli.begin_fill()
tuli.left(90)
for i in range(180):
    tuli.forward(1.1)
    tuli.right(1)
  
tuli.forward(100)
tuli.right(135)
tuli.forward(30)
tuli.left(90)
tuli.forward(30)
tuli.right(90)
tuli.forward(30)
tuli.left(90)
tuli.forward(30)
tuli.right(90)
tuli.forward(30)
tuli.left(90)
tuli.forward(30)
tuli.right(135)
tuli.forward(100)
tuli.end_fill()

tuli.penup()
tuli.goto(40, 0)
tuli.pendown()
tuli.color("black", "white")
tuli.begin_fill()
tuli.circle(12)
tuli.end_fill()

tuli.penup()
tuli.goto(-8, 0)
tuli.pendown()
tuli.color("black", "white")
tuli.begin_fill()
tuli.circle(12)
tuli.end_fill()

tuli.penup()
tuli.goto(300, 0)

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
            radius = input('Radius of circle: ')
            drawCircle(radius)

        if shape = '2':
            os.system('cls')
            length = input('Length of each side of triangle: ')
            drawTriangle(length)
        
    if choice == '2':
        turtle.clear()

turtle.mainloop()
