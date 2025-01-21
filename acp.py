#acp
import turtle

screen = turtle.Screen()
screen.bgcolor("pink")
rhombus = turtle.Turtle()
rhombus.fillcolor("black")

rhombus.begin_fill()

def draw_rhombus(side_length):
    for _ in range(2):
        rhombus.forward(side_length)
        rhombus.left(60)
        rhombus.forward(side_length)
        rhombus.left(120)


side_length = 100
draw_rhombus(side_length)

rhombus.end_fill()

turtle.done()