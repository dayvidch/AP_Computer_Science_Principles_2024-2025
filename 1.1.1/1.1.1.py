import turtle as trtl

#makes a turtle object called painter.
painter = trtl.Turtle()
#makes the turtle 4 times the original size.
painter.turtlesize(4)
#makes the pensize 10.
painter.pensize(10)

#makes a box
for x in range(4):
    painter.forward(50)
    painter.right(90)

#makes circles
painter.circle(20)
painter.circle(30)
painter.circle(40)
painter.circle(50)
wn = trtl.Screen()
wn.mainloop()

#changes the pen color
painter.pencolor("orange")

painter.penup()
painter.goto(123,123)
painter.pendown()

painter.circle(30)