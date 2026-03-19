#   a123_apple_1.py
'''
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(pear_image)
  wn.update()


#-----function calls-----
draw_apple(apple)

wn.mainloop()
'''

'''
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
w = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

# apple falling
def falling_apple():
 x = apple.xcor()
 apple.penup()
 apple.goto(x, -125)

# drawing a
def draw_a():
 w.hideturtle()
 w.penup()
 w.color("white")
 w.goto(apple.xcor() -17, apple.ycor()-40)
 w.write("a", font=("Arial", 74, "bold")) 

#-----function calls-----
draw_apple(apple)
draw_a()
wn.onkeypress(falling_apple, "a")
wn.listen()
wn.mainloop()
'''

'''
import turtle as trtl
import random

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

homerows = ["a","s","d","f","j","k","l",";"]
popped_letter = homerows.pop(random.randint())

apple = trtl.Turtle()
w = trtl.Turtle()
w.hideturtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

# apple falling
def falling_apple():
 x = apple.xcor()
 apple.penup()
 apple.goto(x, -125)
 apple.clear()

 #gets rid of both the apple and letter turtle after the key has been pressed
 apple.hideturtle()
 w.clear()

# drawing a
def draw_a():
 w.hideturtle()
 w.penup()
 w.color("white")
 w.sety(apple.ycor()-50)
#  w.goto(apple.xcor() -17, apple.ycor()+140)
 w.write("a", align="center",  font=("Arial", 74, "bold"))
 w.sety(apple.ycor()+50)

 #   a123_apple_letters.py

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters
letters = ["a", "b", "c", "d", "e", "f", "g"]
total_apples = int(len(letters))
def new_position(apple):
 if letters:
  next_letter = random.choice(letters)
  x = random.randint(-250,250)
  y = random.randint(-10,180)
  apple.goto(x,y)
  return next_letter
 else:
  return None


#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)
def draw_letter(apple, next_letter):
 apple.color("white")
 apple.write(next_letter, font=("Arial", 74, "bold"))


#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen
def apple_setup(apple, letter):
 apple.shape(apple_image)
 next_letter = new_position(apple)
 if next_letter:
  draw_letter(apple, letter)
 wn.update()

 


#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
apple_list = []
for i in range(0,total_apples):
  #Your code here
  new_apple = trtl.Turtle()
  new_apple.penup()
  apple_list.append(new_apple)
  next_letter = new_position(new_apple)
  apple_setup(new_apple, next_letter)


#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.
def drop_apple(letter):
 for apple in apple_list:
  if apple.xcor() == letter[1][0]:  # Check letter position
    apple.goto(-250, -150)
    apple.hideturtle()

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.


#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

def apple_falling():
 for apple in apple_list:
  apple.sety(apple.ycor() - 10)
  if apple.ycor() < -150:
   apple.goto(random.randint(-200, 200), random.randint(100, 250))
   
 


#-----function calls-----
wn.tracer(False)
draw_apple(apple)
draw_letter(apple, "a")

wn.tracer(True)
wn.onkeypress(falling_apple, "a")
wn.onkeypress(falling_apple, "e")


wn.listen()
wn.update()
wn.mainloop()
'''

import turtle as trtl
import random

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple_list = []
apple_letters = []
letters = ["a","s","d","f","j","k","l"]

for x in range(6):
  temporary_apple = trtl.Turtle()
  apple_list.append(temporary_apple)
  apple_letters.append(random.choice(letters))


apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
'''
This function makes the apple, and sets them at a random location on the tree. 
It also sets the letter on top of the apple.
'''
def draw_apple(index):
    apple_list[index].penup()
    apple_list[index].shape(apple_image)
    wn.tracer(False)
    apple_list[index].setx(random.randrange(-175,175))
    apple_list[index].sety(random.randrange(-25,100))
    
    letter = apple_letters[index]
    apple_list[index].sety(apple_list[index].ycor()-35)
    apple_list[index].color("white")
    apple_list[index].write(letter, align="center", font = ("Arial", 40, "bold"))
    apple_list[index].sety(apple_list[index].ycor()+35)
    apple_list[index].showturtle()
    wn.tracer(True)
    wn.update()

# apple falling
'''
This function makes the apple fall down, and gets rid of the apple once it had reached the ground.
It also changes the letter on the apple to a different random letter.
'''
def drop_apple(index):
 apple_list[index].penup()
 apple_list[index].clear()
 apple_list[index].sety(-150)
 #gets rid of both the apple and letter turtle after the key has been pressed
 apple_list[index].hideturtle()
 apple_letters[index] = random.choice(letters)
 draw_apple(index)

'''
Each of the functions below is responsible for if each letter is pressed.
If the letter is pressed, then it calls on the drop_apple function from earlier, which drops the apple.
'''
def pressed_a():
  for x in range(6):
    if apple_letters[x] == "a":
        drop_apple(x)
        break

def pressed_s():
  for x in range(6):
    if apple_letters[x] == "s":
        drop_apple(x)
        break

def pressed_d():
  for x in range(6):
    if apple_letters[x] == "d":
        drop_apple(x)
        break

def pressed_f():
  for x in range(6):
    if apple_letters[x] == "f":
        drop_apple(x)
        break

def pressed_j():
  for x in range(6):
    if apple_letters[x] == "j":
        drop_apple(x)
        break

def pressed_k():
  for x in range(6):
    if apple_letters[x] == "k":
        drop_apple(x)
        break

def pressed_l():
  for x in range(6):
    if apple_letters[x] == "l":
        drop_apple(x)
        break


for x in range(5):
   draw_apple(x)
wn.onkeypress(pressed_a, "a")
wn.onkeypress(pressed_s, "s")
wn.onkeypress(pressed_d, "d")
wn.onkeypress(pressed_f, "f")
wn.onkeypress(pressed_j, "j")
wn.onkeypress(pressed_k, "k")
wn.onkeypress(pressed_l, "l")



wn.listen()
trtl.mainloop()

'''
Question 17

import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

turtle_list = []

temp_turtle = trtl.Turtle()
temp_turtle.pencolor("red")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("blue")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("green")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("pink")
turtle_list.append(temp_turtle)


turtle_list[0].forward(500)
turtle_list[1].setheading(45)
turtle_list[1].forward(500)
turtle_list[2].setheading(315)
turtle_list[2].forward(500)
turtle_list[3].setheading(180)
turtle_list[3].forward(500)
trtl.mainloop()

'''

'''
Question 18

import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

turtle_list = []

temp_turtle = trtl.Turtle()
temp_turtle.pencolor("red")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("blue")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("green")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("pink")
turtle_list.append(temp_turtle)


turtle_list[0].forward(500)
turtle_list[1].setheading(45)
turtle_list[1].forward(500)
turtle_list[2].setheading(315)
turtle_list[2].forward(500)
turtle_list[3].setheading(180)
turtle_list[3].forward(500)
turtle_list[4].forward(400)
trtl.mainloop()

The error was that it was out of range because we do not have 5 turtles in the list. To fix this problem, you have to make another turtle instance,
and append it to the turtle_list.

'''

'''
Question 19

import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

turtle_list = []

temp_turtle = trtl.Turtle()
temp_turtle.pencolor("red")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("blue")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("green")
turtle_list.append(temp_turtle)

temp_turtle = trtl.Turtle()
temp_turtle.pencolor("red")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("blue")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("green")
turtle_list.append(temp_turtle)

turtle_list[0].forward(0)
turtle_list[1].setheading(0)
turtle_list[1].forward(0)
turtle_list[2].setheading(0)
turtle_list[2].forward(0)

turtle_list[3].forward(0)
turtle_list[3].setheading(0)
turtle_list[4].forward(0)
turtle_list[4].setheading(0)
turtle_list[5].forward(0)

degree = 60
for active_turtle in turtle_list:
  active_turtle.setheading(active_turtle.heading()+ degree)
  active_turtle.forward(400)
  degree += 60
  
wn.mainloop()
'''

'''
Question 20

import turtle as trtl
import random

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

number_list = [1,2,3,4]
random.shuffle(number_list)


print(number_list)
# Note the usage of the keyword "in" below.
if (4 in number_list):
  temp_turtle = trtl.Turtle()
  temp_turtle.write("4 in list.", font=("Arial", 74, "bold"))
else:
   temp_turtle = trtl.Turtle()
   temp_turtle.write("4 not in list.", font=("Arial", 74, "bold"))
  

trtl.mainloop()
'''

'''
Conclusion Questions

1. Lists were used  this activity to abstract away detail by picking random letters, and adding modified variables in the other lists
2. The benefits of using functions in this program to abstract away detail were that it made the code easier to follow, and it made it
   easier to work with.
3. New programming features I learned from this activity that I can use in future programs were the onkeypress function and
   using temporary apples. I might see theses features again in the future when I need to make some temporary varaibles to help
   manipulate the main varaible, and when i need to click a turtle for an action to happen.

'''