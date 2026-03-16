import turtle as trtl
import random
import time

wn = trtl.Screen()

# colors = ["black", "grey"] 
# while True:
#     for color in colors:
#         wn.bgcolor(color)
#         time.sleep(.2)

wn.bgcolor("Black")

painter = trtl.Turtle()

#setting the pikachu gif to a varaible
pikachu_image = "pikachu.gif"
wn.addshape(pikachu_image)

#setting the log gif to a variable
pokemon_logo = "pokemonlogo.gif"
wn.addshape(pokemon_logo)

#setting the button gif to a varaible
button_image = "button.gif"
wn.addshape(button_image)

#making the pikachu image
pikachu = trtl.Turtle(shape = pikachu_image)
pikachu.hideturtle()
pikachu.penup()
pikachu.setheading(90)
pikachu.goto(0,0)
pikachu.showturtle()

#making the logo image
logo = trtl.Turtle(shape = pokemon_logo)
logo.hideturtle()
logo.penup()
logo.setheading(90)
logo.goto(0,300)
logo.showturtle()

#making the button image
button = trtl.Turtle(shape = button_image)
button.shapesize(stretch_wid=.2, stretch_len=.2)
button.hideturtle()
button.penup()
button.setheading(90)
button.goto(0,-400)
button.showturtle()
button.onclick(False)

#moving the painter
painter.hideturtle()
painter.penup()
painter.goto(-150, -300)
painter.pendown()

#function to write text
# Chatgpt
def write_text(text, color):
    painter.color(color)
    painter.write(text, font = ("Arial", 60, "normal"))
write_text("Python Ver.", "White")
#Chatgpt



#lightning

# Create an empty list for turtles
lightning_list = []

wn_width = wn.window_width()
amount = int(wn_width / 20)
total_width = amount * 20
print(amount)
print(total_width)

# Starting position
tloc = -600

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
while steps < 5:
    for x in lightning_list:
        x.pendown()
        x.forward(random.randint(50, 100))
        x.setheading(random.randint(200, 225))  # Down-left
        x.forward(random.randint(50, 100))
        x.setheading(random.randint(300, 315))  # Down-right
        x.forward(random.randint(50, 100))

    steps += 1


print("done")

wn.mainloop()