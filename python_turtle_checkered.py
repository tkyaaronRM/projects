import turtle
t = turtle.Turtle()

fillCol = 'white'
y = 0

for row in range(7):
    t.setx(0)
    t.sety(y)

    for c in range(7):
        t.color('black', fillCol)
        t.begin_fill()
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.end_fill()
    
        if fillCol == 'black':
            fillCol = 'white'

        elif fillCol == 'white':
            fillCol = 'black'

        t.forward(20)
    y = y - 20

turtle.mainloop()
