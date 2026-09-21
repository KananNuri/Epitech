import turtle

def draw_polygon(sides):
    pen = turtle.Turtle()
    angle = 360 / sides

    for i in range(sides):
        pen.forward(100)
        pen.right(angle)

draw_polygon(8)

turtle.done()