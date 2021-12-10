import turtle
length = int(input('enter length value'))
breadth = int(input('enter breadth value'))
color = input('enter color')
speed = int(input('enter speed'))
for r in range(0, 2):
    turtle.pencolor(color)
    (turtle.speed(speed))
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(breadth)
    turtle.left(90)

'enter colour'