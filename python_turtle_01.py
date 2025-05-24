import turtle
timu = turtle.Turtle()

timu.color('blue')
timu.pensize(5)

for i in range(360):
    timu.forward(1)
    timu.left(1)

turtle.mainloop()
