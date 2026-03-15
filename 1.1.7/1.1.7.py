### Note for the assignment, and all future assignments. When you give a prediction, I want to know if you were actually correct, if not what did you learn from your original understanding. ###

'''Lists & List Method'''
# 0 What is the difference between a list and array?
'''
While a list could contain an ordered collection of different items and values, and Array is an ordered list of elements of the same type.
'''

# 1 Prediction:
'''
We predit that the terminal would print the list as the output.
''' 

# 2 
'''
We were correct as the terminal did print the list as the output.
'''

'''College Board
Tip: When answering college board topics, try to ask yourself How is it similar/different to python?

'''

# 3 
'''
After the program is ran, 'lion' is appended to the end of the next.
'''

'''College Board'''
'''
College Board uses APPEND(aList, value) to represent adding items to a list.
'''

# 4
'''
After the program is ran, the popped item is printed onto the terminal along a string. In addition, the updated list is printed onto the terminal.
'''

# What is the difference between pop and append?
'''
While pop is used to remove an item from a list, append is used to add a new item into the list.
'''


'''The for Loop'''
# 5 Prediction:
'''
The terminal would output each item from the list on a new line. 
'''

# 6 Did the Prediction Match PERFECTLY (all spaces, brackets, commas, syntax etc.)?

'''
Yes, as each of the items from the list is printed onto a new line on the terminal.
''' 

#  a. While print(new_list) prints a list onto the terminal, the for loop prints each seperate item onto the terminal as a string.'
#  b. For this for loop, it iterates 5 times as there's 5 items on the list.
#  c. For this for loop, the loop variable is "animal".
 


'''College Board'''

'''
FOR EACH item IN a aList
{
  <block of statements>
}
'''


# 7 & 8 Add comments to above code
 
''' 
Each item on the list would be iterated and printed on the terminal as separate strings.
'''
#Definies a list
new_list = ["dog", "cat", "mouse", "bird", "monkey"]
#For each item on the list, it is printed onto the terminal
for animal in new_list: 
  #Prints a string that goes before each item printed
  print("next animal:")
  print(animal)

'''
If two more print statements are added below the for statement, there would be 20 lines of output, 
and 4 lines for each of the 5 iterations.
'''

'''Looping with Lists of Turtles'''

# 9 - 11


#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
'''
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#Defines the variables that initatilizes the x and y coordinates of turtle  
startx = 0
starty = 0

#For each item in the list, it goes to the initalized x and y coordinate, 
# and draws its shape, turns right by 45 degrees, and move forward by 50
for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)     
  t.forward(50)

#Increments the initizalized variables by 50.
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()
'''
 
'''It’s Your Turn'''
# 12 - 18 Copy and paste the final code from #11 and complete 12-18. Make sure to comment your code!

#Add code to make turtles move in a circle and change colors.
import turtle as trtl
import random
# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]


for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.speed(0)
  t.penup()

  random_number = random.randint(0, len(turtle_colors) -1)
  new_color = turtle_colors.pop(random_number)

  t.pencolor(new_color)
  t.fillcolor(new_color)
  t.begin_fill()
  t.end_fill()
  my_turtles.append(t)


#Defines the variables that initatilizes the x and y coordinates of turtle  
startx = 0
starty = 0

#For each item in the list, it goes to the initalized x and y coordinate, 
# and draws its shape, turns right by 45 degrees, and move forward by 50

space = 8
direction = 45
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.setheading(direction)
  t.right(45)     
  t.forward(50 + space)
  direction += 45
  space += 5
  

#Increments the initizalized variables by 50.
  startx = t.xcor()
  starty = t.ycor()


wn = trtl.Screen()
wn.mainloop()



# Quiz Results:

 
'''Conclusion'''
# 1

# 2