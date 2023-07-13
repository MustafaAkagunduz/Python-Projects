import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("board for kids")

kalender = turtle.Turtle()

def turtle_forward():
    kalender.forward(10)

def turn_right():
    kalender.right(10)
    #kalender.setheading(kalender.heading()-10)

def turn_left():
    kalender.left(10)
    #kalender.setheading(kalender.heading()+10)

def clear_screen():
    kalender.clear()

def return_home_baby():
    kalender.penup()
    kalender.home()
    kalender.pendown()

def pen_up():
    kalender.penup()
def pen_down():
    kalender.pendown()
drawing_board.listen()
drawing_board.onkey(fun=turtle_forward , key="space")
drawing_board.onkey(fun=turn_right , key="Right")
drawing_board.onkey(fun=turn_left , key="Left")
drawing_board.onkey(fun=return_home_baby , key="h")
drawing_board.onkey(fun=clear_screen , key="c")
drawing_board.onkey(fun=pen_up , key="q")
drawing_board.onkey(fun=pen_down , key="w")


turtle.mainloop()
