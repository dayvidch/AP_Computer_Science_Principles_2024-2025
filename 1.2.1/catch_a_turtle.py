# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
# setting up the properties for object1
color = "pink"
size = 4
shape = "circle"

# initializes the score to 0
score = 0

# seting up the font
font_setup = ("Arial", 20, "normal")

#setting up my colors list
colors_list = ["black", "blue", "orange", "green"]

#setting up size list
size_list = [0.5, 1.0, 1.5, 2, 2.5, 3, 3.5, 4]

#setting up shape list
shape_list = ["square", "circle", "arrow", "triangle", "turtle", "classic"]

# setting up the game to not be started
start_game = False

#-----initialize turtle-----
# initialize and sets up object1
object1 = trtl.Turtle()
object1.shape(shape)
object1.shapesize(size)
object1.fillcolor(color)

#initialize score label
score_label = trtl.Turtle()
score_label.hideturtle()
score_label.penup()
score_label.goto(520, 400)
score_label.pendown()
score_label.write("score: ", font = font_setup)

# initialize the score display
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(600, 400)
score_writer.pendown()

# setting up the timer properties
timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# initializing the timer
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-600, 400)
counter.pendown()

# initalize the start button
start_btn = trtl.Turtle()
start_btn.fillcolor("red")
start_btn.begin_fill()
start_btn.shape("square")
start_btn.end_fill()
start_btn.shapesize(15)
start_btn.goto(0,0)

# initalize the starting message
start_message = trtl.Turtle()
start_message.hideturtle()
start_message.penup()
start_message.goto(0,200)
start_message.pendown()
start_message.write("Click the red button to Start Game", align="center", font=font_setup)

#-----game functions--------

'''function to start the game'''
def click_start(x, y):
  global start_game
  start_game = True
  start_btn.hideturtle()
  start_message.clear()

'''function to do what you want whenever the object is clicked'''
def object1_clicked(x,y):

  #print("Object1 was clicked")

  add_color()
  change_size()
  change_shape()

  #checks if time up
  if timer_up == False:
    change_position()
    update_score()
  else:
    object1.hideturtle()


'''function to choose a random location for the x and y coordinates. Also has the object leave no trail'''
def change_position():
  new_xpos = rand.randint(-400, 400)
  new_ypos = rand.randint(-300, 300)
  object1.hideturtle()
  object1.penup()
  object1.goto(new_xpos, new_ypos)
  object1.pendown
  object1.showturtle()

'''function to update the score in increments of 1'''
def update_score():
  global score
  score += 1
  #print(score)
  score_writer.clear()
  score_writer.write(score, font = font_setup)

'''function for the timer'''
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

'''function to add color to the shape'''
def add_color():
  object1.fillcolor(rand.choice(colors_list))
  object1.stamp()

'''function to change size of the shape'''
def change_size():
  object1.shapesize(rand.choice(size_list))

'''function to change the shape'''
def change_shape():
  object1.shape(rand.choice(shape_list))

#-----events----------------
wn = trtl.Screen()
wn.bgcolor("grey")
start_btn.onclick(click_start)
while not start_game:
  wn.update()
object1.onclick(object1_clicked)
wn.ontimer(countdown, counter_interval)
  
wn.mainloop()
 