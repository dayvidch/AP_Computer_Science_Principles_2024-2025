import turtle as trtl
import random
import time

papple = trtl.Turtle()
papple_image = "pear.gif"
apple_image = "apple.gif"

number_of_papples = 5

global score
global roundOver
roundOver = False
score = 0

wn = trtl.Screen()
wn.setup(width=800, height=800)
wn.addshape(papple_image)
wn.addshape(apple_image)

def createListofPapples():
  papple1 = trtl.Turtle()
  papple2 = trtl.Turtle()
  papple3 = trtl.Turtle()
  papple4 = trtl.Turtle()
  papple5 = trtl.Turtle()
  list = [papple1, papple2, papple3, papple4, papple5]
  return list


def draw_papple():
  global stopKey
  stopKey = True
  xCoor = -175
  yCoor = 300
  for i in range(0, number_of_papples):
    active_papple = papples[i]
    active_papple.shape(papple_image)
    active_papple.penup()
    active_papple.goto(xCoor, yCoor)
    active_papple.pendown()
    xCoor += 60
  wn.update()

def dropPapple(letterIndex):
  xcor = papples[letterIndex].xcor()
  ycor = papples[letterIndex].ycor()
  while (ycor > -30):
      ycor -= 15
      papples[letterIndex].penup()
      papples[letterIndex].goto(xcor, ycor)
      papples[letterIndex].pendown()
  papples[letterIndex].hideturtle()



  papples[letterIndex].penup()
  papples[letterIndex].goto(-175 + (60 * letterIndex), 300)
  papples[letterIndex].pendown()
  papples[letterIndex].shape(papple_image)
  papples[letterIndex].showturtle()


timer_turtle = trtl.Turtle()
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(150, 150)


#basket setup
basket = trtl.Turtle()
basket.penup()
wn = trtl.Screen()
basket_img = "basket.gif"
wn.addshape(basket_img)
basket.shape(basket_img)
basket.goto(0, -100)

#moving
def move_runner():
  basket.forward(10)

#directions
def up():
    if (stopKey == False):
      basket.setheading(90)
      move_runner()

def down():
  if (stopKey == False):
    basket.setheading(270)
    move_runner()

def left():
  if (stopKey == False):
    basket.setheading(180)
    move_runner()

def right():
  if (stopKey == False):
    basket.setheading(0)
    move_runner()

wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")

def droppappler():
    dropPapple(1)

wn.onkeypress(droppappler, "m")

stopKey = False
startTime = int (time.time())
counter =  trtl.Turtle()
counter_interval = 1000
font_setup = ("Arial", 20, "normal")
timer = 5


def countdown(pappleIndex):
  global stopKey
  global timer, timer_up
  global roundOver
  stopKey = False
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    stopKey = True
    dropPapple(pappleIndex)
    # if papples[1].ycor() < 50:
    if basket.xcor() - 30 < papples[pappleIndex].xcor() < basket.xcor() + 30:
      print("hi")
      global score
      score += 1
      score_writer.clear()
      score_writer.write("Score: " + str(score), font=font_setup)
      roundOverGame(True)
    else:
      roundOverGame(False)
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(lambda: countdown(pappleIndex), counter_interval) 

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-100,0)
score_writer.write("Score: " + str(score), font=font_setup)


wn.listen()

papples = createListofPapples()

import random
def pick_papple(papples):
  currentPappleIndex = random.randint(0, len(papples)-1)
  papples[currentPappleIndex].shape(apple_image)
  return currentPappleIndex


def roundOverGame(gameOver):
  if gameOver == True:
    global timer
    timer = 5
    game()


draw_papple()


def game():
    currentPappleIndex = pick_papple(papples)
    i = countdown(currentPappleIndex)
     


game()


endTime = int (time.time())
print(endTime - startTime)

wn.mainloop()