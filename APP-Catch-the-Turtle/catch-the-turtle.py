import turtle
import random

#GAME SCREEN
game_screen= turtle.Screen()
game_screen.bgcolor("green")
game_screen.title("Catch the turtle")

score_board = turtle.Turtle() #initializing the score board
time_board = turtle.Turtle() #initializing the timer board

FONT = ("Arial", 30, "normal") #CONSTANT TUPLE FOR TEXT
grid_size = 10 #Variable, in case of increasing the game area
turtle_list = []
current_score = 0
game_over = False

def setup_score_board():

    #SCORE BOARD

    score_board.hideturtle() #in order not to see the line-drawer
    score_board.color("white") #color ot the table
    score_board.penup() #avoid drawing a line to the top

    #putting board to the right position
    top_height = game_screen.window_height() / 2
    yAxis = top_height * 0.9
    score_board.setpos(0,yAxis)
    #content
    score_board.write(arg="Score: 0", move= False, align= "center",font= FONT)
def setup_countdown_table(time):

    global game_over
    #TIMER BOARD
    time_board.hideturtle() #in order not to see the line-drawer
    time_board.color("white") #color ot the table
    time_board.penup() #avoid drawing a line to the top

    #putting board to the right position
    top_height = game_screen.window_height() / 2
    yAxis = top_height * 0.9
    time_board.setpos(0,yAxis-30)
    time_board.clear()
    #content
    if time>0:
        time_board.clear()
        time_board.write(arg=f"Time: {time}", move= False, align= "center",font= FONT)
        game_screen.ontimer(lambda: setup_countdown_table(time-1), 1000)
    else:
        game_over = True
        time_board.clear()
        hide_turtles()
        time_board.write(arg="GAME OVER", move= False, align= "center",font= FONT)
def create_turtle(xAxis , yAxis):
    t = turtle.Turtle()
    #what happens if we click the turtles
    def click_operations(xCoord,yCoord):
        global current_score
        current_score += 1
        global score_board
        score_board.clear()
        score_board.write(arg=f"Score: {current_score}", move= False, align= "center",font= FONT)

        #print(xCoord,yCoord)
    t.onclick(click_operations) #event listener
    t.shape("turtle")
    t.color("white")
    t.shapesize(2,2) #times of default size 1
    t.penup()
    t.goto(xAxis*grid_size, yAxis*grid_size)
    turtle_list.append(t)
def setup_turtle_positions():
    x_coordinates = [-20,-10,0,10,20]
    y_coordinates = [-20,-10,0,10,20]

    for x in x_coordinates:
        for y in y_coordinates:
            create_turtle(x,y)
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        game_screen.ontimer(show_turtles_randomly, 500) #recursive funct.
def start_the_game():

    turtle.tracer(0) #Cancels the intro animations
    setup_score_board()
    setup_countdown_table(10)
    setup_turtle_positions()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1) #Cancels the intro animations

start_the_game()

#END
turtle.mainloop()
