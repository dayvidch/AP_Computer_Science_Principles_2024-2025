import turtle as trtl
import random
import time

wn = trtl.Screen()

wn.bgcolor("Black")

painter = trtl.Turtle()

#setting the button gif to a varaible
button_image = "button.gif"
wn.addshape(button_image)

#making the button image
button = trtl.Turtle(shape = button_image)
button.hideturtle()
button.penup()
button.setheading(90)
button.goto(0,0)
button.showturtle()
button.onclick(False)