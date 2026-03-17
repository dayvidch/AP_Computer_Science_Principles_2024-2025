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

#-----initialize turtle-----
# initialize and sets up object1
object1 = trtl.Turtle()
object1.shape(shape)
object1.shapesize(size)
object1.fillcolor(color)

# initialize the score display
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, -300)
score_writer.pendown()

# setting up the timer properties
timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# initializing the timer
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-50, 300)
counter.pendown()

#-----game functions--------
'''function to do what you want whenever the object is clicked'''
def object1_clicked(x,y):
  #print("Object1 was clicked")

  
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


#-----events----------------

object1.onclick(object1_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()