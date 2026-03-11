#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 21

# iterate
for floor in range(num_floors):
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  color = floor % 3
  if (color == 0):
    painter.color("black")
  elif (color == 1):
    painter.color("orange")
  else:
    painter.color("yellow")
  y = y + 5 # location of next floor

  #draw the floor
  painter.pendown()
  painter.forward(50)

x = -90
y = -150
for floor in range(num_floors):
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  color = floor % 3
  if (color == 0):
    painter.color("black")
  elif (color == 1):
    painter.color("orange")
  else:
    painter.color("yellow")
  y = y + 5 # location of next floor

  #draw the floor
  painter.pendown()
  painter.forward(50)

x = -30
y = -150
for floor in range(num_floors):
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  color = floor % 3
  if (color == 0):
    painter.color("black")
  elif (color == 1):
    painter.color("orange")
  else:
    painter.color("yellow")
  y = y + 5 # location of next floor

  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()