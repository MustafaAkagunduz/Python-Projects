import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("red")
turtle_screen.title("Turtle Shrinking Sauare")

kalender = turtle.Turtle()
kalender.color("yellow")

#opt-1

def shrinkingSquare(size):
    while True:
        kalender.forward(size)
        kalender.left(90)
        size -=10

        if size == 10:
            break



shrinkingSquare(200)

turtle.done
