import turtle as trtl
import time
import random

wn = trtl.Screen()
#Sets the background color to custom green color
wn.bgcolor("#cefad0")
painter = trtl.Turtle()
painter.penup()
painter.hideturtle()
painter.speed(0)
painter.goto(-200,-200)
painter.pendown()
for i in range(2):
  painter.begin_fill()
  painter.fillcolor("white")
  painter.forward(350)
  painter.right(90)
  painter.forward(80)
  painter.right(90)
  painter.end_fill()

def fight_option():
  painter.penup()
  painter.goto(-160, -250)
  painter.pendown()
  painter.write("FIGHT", font=("Futura", 20, "bold"))

def run_option():
  painter.penup()
  painter.goto(40, -250)
  painter.pendown()
  painter.write("RUN", font=("Georgia", 20, "bold"))
  painter.penup()

fight_option()
run_option()
user_hp = 100
robot_hp = 100




while True:
  message3 = trtl.textinput(title="Options", prompt="Fight or Run?:")

  if(message3 == "Fight" or message3 == "fight"):
    wn.clearscreen()
    wn.bgcolor("#cefad0")
    painter = trtl.Turtle()
    painter.penup()
    painter.hideturtle()
    painter.speed(0)
    painter.goto(-200,-200)
    painter.pendown()
    for i in range(2):
      painter.begin_fill()
      painter.fillcolor("white")
      painter.forward(350)
      painter.right(90)
      painter.forward(80)
      painter.right(90)
      painter.end_fill()
    fight_option()
    painter.penup()
    painter.goto(-120, -320)
    painter.pendown()
    painter.pensize(5)
    painter.color("red")
    painter.circle(80)
    attack = random.randint(25,100)
    if attack >= 60:
      print("critical hit")
    robot_hp -= attack
    print(robot_hp)
    break

  elif(message3 == "Run" or message3 == "run"):
    wn.clearscreen()
    wn.bgcolor("#cefad0")
    painter = trtl.Turtle()
    painter.penup()
    painter.hideturtle()
    painter.speed(0)
    painter.goto(-200,-200)
    painter.pendown()
    for i in range(2):
      painter.begin_fill()
      painter.fillcolor("white")
      painter.forward(350)
      painter.right(90)
      painter.forward(80)
      painter.right(90)
      painter.end_fill()
    run_option()
    painter.penup()
    painter.goto(70, -320)
    painter.pendown()
    painter.pensize(5)
    painter.color("red")
    painter.circle(80)
    break
  
  else:
    True



wn.mainloop()