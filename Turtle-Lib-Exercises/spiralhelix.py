import turtle

turtle_screen= turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Circular")

kalender = turtle.Turtle()
kalender.color("white")
kalender.speed(0) #en hızlısı

kalender_colors = ["red", "purple", "blue", "green", "orange", "yellow"]

r = 80
i = 0
while True:

    kalender.color(kalender_colors[i%6])


    kalender.circle(r)
    kalender.circle(-r)
    kalender.left(i)

    r -= 5
    i += 1

    if r==10:
        break

turtle.mainloop()
#turtle.done()

