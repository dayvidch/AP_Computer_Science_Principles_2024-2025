import turtle as trtl
import random
import time

# Create a screen object
wn = trtl.Screen()

# Create an empty list for turtles
lightning_list = []

# Starting position
wn_width = wn.window_width()
amount = int(wn_width / 20)
total_width = amount * 20
print(amount)
print(total_width)

tloc = -400

# Creating the turtles
for x in range(amount):
    # Create vertical turtles
    lightning = trtl.Turtle()  # Instantiate the turtle object
    lightning.turtlesize(0.5)  # Set the size
    lightning.fillcolor("yellow")  # Set fill color
    lightning.pencolor("Yellow")
    lightning.pensize(10)
    lightning.penup()
    lightning.goto(-tloc, 300)  # Position the turtle
    lightning.setheading(270)  # Face down
    lightning_list.append(lightning)  # Add turtle to the list
    tloc += 100  # Update position

# Move turtles across and down the screen
steps = 0
while steps < 30:
    for x in lightning_list:
        x.pendown()
        x.forward(random.randint(100, 200))
        x.setheading(random.randint(200, 225))  # Down-left
        x.forward(random.randint(100, 200))
        x.setheading(random.randint(300, 315))  # Down-right
        x.forward(random.randint(10, 200))

    steps += 1

wn.mainloop() 
