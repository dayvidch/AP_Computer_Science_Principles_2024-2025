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
    time.sleep(2)
    False
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
    time.sleep(2)
    False
    break
  else:
    True
    break
  

wn.clearscreen()
wn.bgpic("welcome.gif")
wn.bgcolor("black")

username = message1
gender = message2
if gender =="m":
   gender = "Man"
else:
    gender = "Woman"

def story_text(text):
    painter.color("Black")
    painter.write(text, font = ("Arial", 30, "italic"))

x = -375
y = 280
painter.penup()
painter.goto(x,y)
painter.pendown()
time.sleep(1)
story_text("Welcome to the world of Pokemon " + username,)
painter.penup
y = y - 50
time.sleep(1)

painter.goto(x,y)
painter.pendown()
story_text("You are becoming a young " + gender + " now",)
painter.penup
y = y - 50
time.sleep(1)

painter.goto(x,y)
painter.pendown()
story_text("Lets see if you have what it takes?")
painter.penup
y = y - 50
time.sleep(3)

wn.clearscreen()
y = 300

wn.bgpic("decision.gif")

def rectangle():
    for i in range(2):
        painter.begin_fill()
        painter.fillcolor("white")
        painter.forward(900)
        painter.right(90)
        painter.forward(200)
        painter.right(90)
        painter.end_fill()
        painter.up()

painter.goto(-450,375)
rectangle()

painter.goto(-400, y)
story_text("With all the pokemon in the world, I'll give you my favorite one.")
time.sleep(1)
y = y - 50
painter.up()
painter.goto(-400, y)
story_text("Just kidding, you took too long, and this is the last one.")
time.sleep(1)
y = y - 50
painter.up()
painter.goto(-400, y)
story_text("You get Pikachu.")
time.sleep(2)

user_pokemon = "funnyPikachu.gif"
wn.addshape(user_pokemon)

#making the pikachu image
user_pokemon = trtl.Turtle(shape = user_pokemon)
user_pokemon.hideturtle()
user_pokemon.penup()
user_pokemon.setheading(90)
user_pokemon.goto(0,-30)
user_pokemon.showturtle()

painter.goto(-450, -250)
rectangle()

painter.goto(-200, -350)
story_text("Ready for your first battle?!")
wn = trtl.Screen()
wn.mainloop()