#activity3
import turtle

turtle.Screen().bgcolor("yellow")
polygon = turtle.Turtle()
polygon.fillcolor("pink")
polygon.begin_fill()

num_sides = 7
side_length = 70
angle = 360 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

polygon.end_fill()

turtle.done()