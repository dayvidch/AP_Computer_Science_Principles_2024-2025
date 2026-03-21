import turtle as trtl
import random as rand

#Maze functions
def draw_door():
    maze_painter.penup()
    maze_painter.forward(door_length)
    maze_painter.pendown()
    maze_painter.forward(second_half)

def draw_barrier():
    maze_painter.back(second_half)
    maze_painter.right(90)
    maze_painter.forward(barrier_length)
    maze_painter.back(barrier_length)
    maze_painter.left(90)
    maze_painter.forward(second_half)
    maze_painter.right(90)

#Runner functions

#directions
def up():
    Fortnite_runner.setheading(90)

def down():
    Fortnite_runner.setheading(270)

def left():
    Fortnite_runner.setheading(180)

def right():
    Fortnite_runner.setheading(0)

#moving
def move_runner():
  Fortnite_runner.forward(10)

#timer function
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font="arial")
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font="arial")
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#pause screen
def pause_screen():
   wn.clearscreen()


#start/stop
def start_stop():
   button.speed(0)
   button.begin_fill()
   button.fillcolor("red")
   button.shape("square")
   button.shapesize(5)
   button.end_fill()
   button.penup()
   button.goto(600,0)
   button.onclick(pause_screen)



#General setup 
wn = trtl.Screen()

#start/stop button
button = trtl.Turtle()

# initalize the starting message
start_message = trtl.Turtle()
start_message.hideturtle()
start_message.penup()
start_message.goto(600,50)
start_message.pendown()
start_message.write("Click the red button to Pause the game", align="center")

#Maze setup
maze_painter = trtl.Turtle()
maze_painter.hideturtle()
maze_painter.pensize(3)
maze_painter.speed(0)

side_length = 10
door_length = 50
barrier_length = 50

#Drawing the maze
for x in range(20):
    if x in range(3):
        maze_painter.penup()
    else:
        maze_painter.pendown()

        for x in range(2):
            total_side_length = side_length/2
            first_half = rand.randrange(int(total_side_length))
            second_half = total_side_length - first_half
            maze_painter.forward(first_half)

            #Doors
            draw_door()

            #Barriers
            draw_barrier()

            #Increment each side
            side_length += 50

#Maze Runner Setup
Fortnite_runner = trtl.Turtle()
Fortnite_image = "medium.gif"
wn.addshape(Fortnite_image)
Fortnite_runner.shape(Fortnite_image)

# setting up the timer properties
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# initializing the timer
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-600, 400)
counter.pendown()


#function calls

#directions
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")

#moving
wn.onkeypress(move_runner," ")

#timer
wn.ontimer(countdown, counter_interval)

#start/stop
start_stop()

wn.listen()
wn.mainloop()
