
import turtle as trtl
painter = trtl.Turtle()

#option 1
for x in range(2):
    painter.forward(100)
    painter.right(90)
    painter.forward(200)
    painter.right(90)

painter.penup()
painter.goto(-150, 0)
painter.pendown()

#option 2
painter.forward(100)
painter.right(90)
painter.forward(200)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(200)
painter.right(90)

wn = trtl.Screen()
wn.mainloop()