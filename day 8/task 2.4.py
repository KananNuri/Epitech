import turtle

pen = turtle.Turtle()

for i in range(100):
    pen.forward(i * 3)
    pen.right(90)

turtle.done()