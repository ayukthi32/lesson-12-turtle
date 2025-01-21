#activivty2
import turtle

turtle.Screen().bgcolor("yellow")
board = turtle.Turtle()
board.fillcolor("pink")
board.begin_fill()

board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.end_fill()

board.penup()
board.right(150)
board.forward(50)

board.begin_fill()

board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)
board.right(120)

board.end_fill()

turtle.done()