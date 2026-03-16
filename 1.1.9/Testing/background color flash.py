import turtle as trtl
import random
import time

wn = trtl.Screen()

# black, grey
colors = ["black", "grey"] 
while True:
    for color in colors:
        wn.bgcolor(color)
        time.sleep(.2)
