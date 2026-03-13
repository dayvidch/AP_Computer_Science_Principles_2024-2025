#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
# creates spiderbody
painter.pensize(40)
painter.circle(20)
# configure spider legs
legs = 8
leg_lenght = 70
dirrection_of_leg = 360 / legs
painter.pensize(5)
legs_currently = 0
# Draws spider legs
while (legs_currently < legs / 2):
  painter.goto(0,20)
  painter.setheading((dirrection_of_leg - 20)*legs_currently - 45)
  print(dirrection_of_leg*legs_currently - 45)
  painter.forward(leg_lenght)
  legs_currently = legs_currently  + 1

while (legs_currently > legs / 2):
    painter.goto(0,20)
    painter.setheading((dirrection_of_leg - 20)*legs_currently + 45)
    print(dirrection_of_leg*legs_currently + 45)
    painter.forward(leg_lenght)
    legs_currently = legs_currently  + 1

painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()