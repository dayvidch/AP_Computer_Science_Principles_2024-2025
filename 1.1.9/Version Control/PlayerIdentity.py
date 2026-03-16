import turtle as trtl
import time

painter = trtl.Turtle()
wn = trtl.Screen()

#Changes the background color to a off-white color
wn.bgcolor("#FFFFE4")
painter.speed(0)
painter.penup()
painter.goto(-300,100)
c = 20
painter.hideturtle()
x = painter.xcor()
y = painter.ycor()
painter.penup()

for i in range(2):
  painter.begin_fill()
  painter.fillcolor("#664228")
  painter.forward(550)
  painter.right(90)
  painter.forward(150)
  painter.right(90)
  painter.end_fill()

painter.penup()
ax = x + 8
ay = y - 8
painter.goto(ax, ay)
painter.pendown()
for i in range(2):
  painter.begin_fill()
  painter.fillcolor("white")
  painter.forward(550 - c)
  painter.right(90)
  painter.forward(150 - c)
  painter.right(90)
  painter.end_fill()



painter.penup()
painter.goto(0,0)
painter.pendown()
trtl.Screen()
message1 = trtl.textinput(title="Player Name", prompt="Insert User name:")

painter.penup()
painter.goto(-280, 55)
painter.write("User_Name ——→", font=("Times New Roman", 15, "bold"))
painter.penup()

painter.goto(-100,57)

def write_text(text, color):
    painter.color(color)
    painter.write(text, font = ("Georgia", 13, "italic"))
write_text(message1, "Black")

while True:
  message2 = trtl.textinput(title="Player Gender", prompt="Insert M/F:")

  if message2.lower() == "m":
    painter.penup()
    painter.goto(-280, 28)
    painter.write("User_Gender ——→", font=("Times New Roman", 15, "bold"))
    painter.penup()
    painter.goto(-70, 28)
    def write_text(text, color):
        painter.color(color)
        painter.write(text, font = ("Arial", 13, "italic"))
    write_text("Male", "Blue")
    break

  elif message2.lower() == "f":
    painter.penup()
    painter.goto(-280, 28)
    painter.write("User_Gender ——→", font=("Arial", 15, "bold"))
    painter.penup()
    painter.goto(-70, 28)
    def write_text(text, color):
        painter.color(color)
        painter.write(text, font = ("Arial", 13, "italic"))
    write_text("Female", "Red")
    break

  else:
    True


wn = trtl.Screen()
wn.mainloop()