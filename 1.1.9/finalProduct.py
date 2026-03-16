#Imports the Libraries that would be used in this software
import turtle as trtl
import random
import time

wn = trtl.Screen()
# wn.screensize(canvheight=400, canvwidth=300)
wn.bgcolor("Black")

painter = trtl.Turtle()
painter.speed(0)
#setting the pikachu gif to a varaible
pikachu_image = "pikachu.gif"
wn.addshape(pikachu_image)

painter.hideturtle()

#setting the log gif to a variable
pokemon_logo = "pokemonlogo.gif"
wn.addshape(pokemon_logo)
button_shape = "button.gif"
wn.addshape(button_shape)

# Create an empty list for turtles
lightning_list = []

wn_width = wn.window_width()
amount = int(wn_width / 20)
total_width = amount * 20
print(amount)
print(total_width)

# Starting position
tloc = -600
painter.speed(0)
# Creating the turtles
for x in range(20):
  lightning = trtl.Turtle()  # Instantiate the turtle object
  lightning.hideturtle()
  lightning.speed(0)
  lightning.turtlesize(0.5)  # Set the size
  lightning.fillcolor("yellow")  # Set fill color
  lightning.pencolor("Yellow")
  lightning.pensize(10)
  lightning.penup()
  lightning.goto(tloc, 450)  # Position the turtle
  lightning.setheading(270)  # Face down
  lightning_list.append(lightning)  # Add turtle to the list
  tloc += 100  # Update position

# Move turtles across and down the screen
steps = 0
while steps < 3:
  for x in lightning_list:
    x.pendown()
    x.forward(random.randint(50, 100))
    x.setheading(random.randint(200, 225))  # Down-left
    x.forward(random.randint(50, 100))
    x.setheading(random.randint(300, 315))  # Down-right
    x.forward(random.randint(50, 100))
  steps += 1



pikachu = trtl.Turtle(shape = pikachu_image)
pikachu.hideturtle()
pikachu.penup()
pikachu.setheading(90)
pikachu.goto(0,0)
pikachu.showturtle()

#making the logo image
painter.hideturtle()
logo = trtl.Turtle(shape = pokemon_logo)
logo.hideturtle()
logo.penup()
logo.setheading(90)
logo.goto(0,300)
logo.showturtle()

painter.hideturtle()
painter.penup()
painter.goto(-150, -300)
painter.pendown()

#function to write text
def write_text(text, color):
  painter.color(color)
  painter.write(text, font = ("Futura", 60, "normal"))
write_text("PYTHON VER.", "White")

#Alternates the background color
for i in range(30):
  wn.bgcolor("black")
  time.sleep(0.2)
  wn.bgcolor("gray")

wn.bgcolor("yellow")

continue_screen = 0
button_shape = "button.gif"
wn.addshape(button_shape)


button = trtl.Turtle(shape = button_shape)
button.hideturtle()
button.penup()
button.setheading(90)
button.goto(0, -400)
button.showturtle()

def load_screen2():
  painter = trtl.Turtle()
  painter.hideturtle()
  global message1
  global message2
  time.sleep(1)
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
  painter.pendown()
  painter.write("User_Name ——→", font=("Times New Roman", 15, "bold"))
  painter.penup()
  painter.goto(-100,57)

  def write_text(text, color):
    painter.color(color)
    painter.write(text, font = ("Futura", 13, "italic"))
  write_text(message1, "Black")

  while True:
    message2 = trtl.textinput(title="Player Gender", prompt="Insert M/F:")
    if message2.lower() == "m":
      painter.penup()
      painter.goto(-280, 28)
      painter.write("User_Gender ——→", font=("Times New Roman", 15, "bold"))
      painter.penup()
      painter.goto(-70, 28)
      def write_male_text(text, color):
        painter.color(color)
        painter.write(text, font = ("Futura", 13, "italic"))
      write_male_text("Male", "Blue")
      print(message1)
      break

    elif message2.lower() == "f":
      painter.penup()
      painter.goto(-280, 28)
      painter.write("User_Gender ——→", font=("Times New Roman", 15, "bold"))
      painter.penup()
      painter.goto(-70, 28)
      def write_female_text(text, color):
        painter.color(color)
        painter.write(text, font = ("Futura", 13, "italic"))
      write_female_text("Female", "Red")
      print(message1)
      break

    else:
      True

def click_button(x,y):
  if (x > -120 and x < 120 and y < -350 and y > -420):
    wn.clearscreen()
    load_screen2()
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
    story_text("Welcome to the world of Pokemon, " + username,)
    painter.penup
    y = y - 50
    time.sleep(3)

    painter.goto(x,y)
    painter.pendown()
    story_text("You are becoming a young " + gender + " now",)
    painter.penup
    y = y - 50
    time.sleep(3)

    painter.goto(x,y)
    painter.pendown()
    story_text("Lets see if you have what it takes?")
    painter.penup
    y = y - 50
    time.sleep(2)

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

wn.onscreenclick(click_button)

wn.mainloop()