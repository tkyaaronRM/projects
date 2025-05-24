import turtle
john = turtle.Turtle()

def clock():
  john.pensize(3)
  john.color("blue")
  for i in range(12):
    john.penup()
    john.forward(70)
    john.pendown()
    john.forward(20)
    john.penup()
    john.backward(90)
    john.left(30)

def star():
  colors = ["blue", "red", "orange", "green", "purple"]
  index = 0
  distance = 7
  for i in range(20):
    if index != 4:
      index = index + 1
      john.color(colors[index])
    else:
      index = 0
      john.color(colors[index])
    john.forward(distance)
    john.left(144)
    distance = distance + 7
  john.forward(56)
  john.penup()
  john.goto(500,0)

def chessboard():
  def black_box():
    john.color('black')
    john.begin_fill()
    for i in range(4):
      john.forward(10)
      john.left(90)
    john.end_fill()

  def white_box():
    for i in range(4):
      john.forward(10)
      john.left(90)

  def move_up():
    john.left(90)
    john.forward(10)
    john.right(90)

  def black_first():
    for i in range(4):
      black_box()
      move_up()
      white_box()
      move_up()

  def white_first():
    for i in range(4):
      white_box()
      move_up()
      black_box()
      move_up()

  def go_down():
    john.right(90)
    john.forward(80)
    john.left(90)
    john.forward(10)

  for i in range(4):
    black_first()
    go_down()
    white_first()
    go_down()

chessboard()

def snowflake():
  def small_petal():
    john.forward(25)
    for i in range(6):
      john.right(60)
      john.forward(10)
      john.backward(10)
    john.backward(25)

  def petal():
    john.forward(80)
    for i in range(6):
      john.right(60)
      small_petal()
    john.backward(80)

  john.pensize(3)
  for i in range(6):
    john.right(60)
    petal()

turtle.mainloop()
