#   Add your code here and add comments to your code 
#   to describe what each section of code is doing

import turtle as trtl
painter = trtl.Turtle()

#allows me to use rgb
trtl.colormode(255)

#relocating the painter
painter.penup()
painter.goto(-50,-20)
painter.pendown()

# first im going to make the stump
painter.fillcolor("brown")
painter.begin_fill()

for x in range(2):
    painter.forward(100)
    painter.right(90)
    painter.forward(200)
    painter.right(90)

painter.end_fill()

#second im going to make the leaves
#leaf 1
painter.fillcolor("green")
painter.begin_fill()
painter.right(180)
painter.penup()
painter.goto(100,-40)
painter.pendown()
for x in range(3):
    painter.forward(200)
    painter.right(120)
painter.end_fill()

#leaf 2
painter.fillcolor((120, 180, 144)) #144
painter.begin_fill()
painter.penup()
painter.goto(100,20)
painter.pendown()
for x in range(3):
    painter.forward(200)
    painter.right(120)
painter.end_fill()

#leaf 3
painter.fillcolor((130, 200, 144))
painter.begin_fill()
painter.penup()
painter.goto(100,80)
painter.pendown()
for x in range(3):
    painter.forward(200)
    painter.right(120)
painter.end_fill()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()