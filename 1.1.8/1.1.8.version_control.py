'''Conditionals & The if statement'''
# 1. Prediction:
'''
1. The code will ask for a number. 
2. If the number is bigger than or equal to 90, then it will print "Input is 90 or more"
'''
# 2. Did the program work exactly like you thought it would? 
'''
Yes, the program worked exactly like I thought it would.
'''
# 3
'''
1. The code will ask for a number
2. If the number is bigger or eqaul to 90, then the code prints "Input is 90 or more"
3. If the number is less than  90, then it prints "Input is less than 90"
My predition was correct.
'''

'''Nested Conditionals''' 
# 4.
'''
If you enter 12 for the year, it satisfies the first conditional statment and moves on the the next condition statement,
which is checking if the number you put is bigger or eqaul to 60. Since you enetered 75, that also satisfies that conditional statement,
which leads to printing "You may graduate".
'''
# 5. 
'''
year = int(input("Enter your year in school -> "))
if (year == 12):
  num_score = int(input("Enter your final score -> "))
  if (num_score >= 60):
    print("You may graduate!")
  else:
    print("Summer school?")
'''
# 6.
'''
1. It will ask for your year in school. The conditional statment is only met if the input is 12.
2. It will then ask for your final score.
3. If the input is greater or equal to 60, then it will say that you can graduate.
4. If the input is less than 60, then it will ask if the course it is required to graduate.
5. If the input for that is n (no), then it will say that you can graduate. 
6. If the input for that is y (yes), then it will recommend summer school. 
My prediction was correct.
'''
# 7.
'''
1. The code will ask for a number.
2. If the number is is greater than or equal to 90, then it will say that the input is 90 or more.
3. If the number is less than 90, it will check if it was bigger than 80. If it was, then will will say that it was 80 or more.
4. If the number is less than 80, it will check if it was bigger than 70. If it was, then will will say that it was 70 or more.
5. If the number is less than 70, it will check if it was bigger than 60. If it was, then will will say that it was 60 or more.
6. If your number was less than 60, will will say that the inout was less than 60.
My prediction was correct.
'''
 
'''The elif Statement'''
# 8 & 9.
'''
Question 8
The two codes do the same thing, but the second version is shorter than the first. 
The second code is also a lot simplier compaierd to the first one.

Question 9
num = int(input("Enter a number -> "))
if (num >= 95):
  print("A")
elif (num >= 85):
  print("B")
elif (num >= 75):
  print("C")
elif (num >= 65):
  print("D")
else:
  print("F")
'''
# 10 & 11.
'''
Quesiont 10
If the number is less than 60, it will do nothing. If the number is greater or equal to 60,
it will always print "D" because it satifies that condition and stops there.

Question 11
I predicted the correct results.
'''

'''
College Board - refers to conditional executions as "selections" because you are selecting a path of execution.
College Board Notation:
  if(condition)
  {
    <block of statements>
  }
  else
  {
    <block of statements>
  }
'''

'''Nested for loop Iteration'''
# 12-14. 
# Prediction:
'''
Question 12
I predict that it will the output will be all the classes everyday.
For example: 
  Monday English Math CS 
  Tuesday Englsih Math CS
  etc.

Question 13
My prediction was inncorect. I had the correct outputs, but they were in the wrong format.
The correct format is:
Monday
  english
  math
  cs
Tuesday
  english
  math
  cs
etc.

Question 14
1. Each element in days_of_week is the outer loop
2. Each element in my_course is the inner loop
3. The Each element in the outer loop prints once
4. For each iteration of the outer loop, the inner loop prints all values in the list.
The total iterations that occured was 15.
'''
# Did the program work exactly like you thought it would? 
'''
The program did not work exactly like I thought. I thought that one iteration of the outer loop and all the inner loops were all on the same line.
I was wrong, the outer loop prints, then the inner loop prints under it.
'''
 

'''Nested Loops and Conditionals'''

# 15 through 17. Program & Test your code for a couple examples in the terminal then summerize your results: 

#   a118_grades.py
#   This code is incomplete. 

'''
for each of the courses taken
  enter a number grade
  display the corresonding letter grade

if you want to redo the grades
  start over
else
  program ends
'''

'''
my_courses = ["English", "Math", "CS"]

for course in my_courses:
  print() # blank line
  print("Enter your points for " + course)

  points = int(input("Points -> "))

  if (points >= 90):
    print("A")
  elif (points >= 80):
    print("B")
  elif (points >= 70):
    print("C")
  elif (points >= 60):
    print("D")
  else:
    print("F")

  redo = "y"
  while (redo == "y"):
    redo = input("Do you need to re-do these grades? (y/n)")
'''
'''
Summary
  The code ask for a number grade for each class, then it gives out the letter grade, corresponding to the number.
  It then asks if the user wants to enter a different grade. 
'''


'''Turtles Stop!'''
# 18 through 20 use the code below (made changes from the original so it would fit in replt.

# a118_turtles_in_traffic.py
# Move turtles horizontally and vertically across screen.
# Stopping turtles when they collide.

'''
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = -95
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  ht.turtlesize(.5)
  #ht.speed(2)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-115, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vt.turtlesize(.5)
  #vt.speed(2)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 115)
  vt.setheading(270)
  
  tloc += 35

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 30:
  for v_turtle in vert_turtles:
    v_turtle.forward(10)
  for h_turtle in horiz_turtles:
    h_turtle.forward(10)  
    if abs(v_turtle.xcor() - h_turtle.xcor()) < 20:
      if abs(v_turtle.ycor() - h_turtle.ycor()) < 20:
       vert_turtles.remove(v_turtle)
       horiz_turtles.remove(h_turtle)
  steps += 1
wn = trtl.Screen()
wn.mainloop()
'''

'''It’s Your Turn'''
# 21 through 22 copy and paste the completed code from the above section and make all the modifications you can.

import turtle as trtl
import random
import time

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
all_colors = horiz_colors + vert_colors

#makes order of everything random
random.shuffle(turtle_shapes)
random.shuffle(horiz_colors)
random.shuffle(vert_colors)

#starting position
tloc = -95

#creating the turtles
for s in turtle_shapes:
  
  #creates the horizontal turtles
  ht = trtl.Turtle(shape=s)
  ht.turtlesize(.5)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-115, tloc)
  ht.setheading(0)

  #creates vertical turtles
  vt = trtl.Turtle(shape=s)
  original_vt = vt.shape()
  vt.turtlesize(.5)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 115)
  vt.setheading(270)
  
  tloc += 35

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 30:

  #random speed
  for v_turtle in vert_turtles:
    v_turtle.forward(random.randint(1,20))
  for h_turtle in horiz_turtles:
    h_turtle.forward(random.randint(1,20)) 

    #detecting the collisions 
    if abs(v_turtle.xcor() - h_turtle.xcor()) < 20:
      if abs(v_turtle.ycor() - h_turtle.ycor()) < 20:
       vert_turtles.remove(v_turtle)
       horiz_turtles.remove(h_turtle)

      #makes random collisions
       collision_shape = turtle_shapes.pop(random.randint(0, len(turtle_shapes) - 1))
       v_turtle.shape(collision_shape)
       v_turtle.turtlesize(2)

      #random collision color
       v_turtle.color(random.choice(all_colors))
       v_turtle
    
  steps += 1
wn = trtl.Screen()
wn.mainloop()




# Explain the changes you made:
'''
We randomized the shapes and colors of each turtle, making the output to look different each time the program ran. In addition, we added an animation that occured each time the turtle
collided with one another. Then, the turtle would return back to its previous state to continue on its path.
'''

# Explain the changes you attempted but could not get to work (if any)
'''
We tried to keep the turtle going after the animation was finished. However, one of the turtles after colliding would just stop, because it is removed from the list. 
'''

# Quiz: 3/3


# Skip AP review section
 
'''Conclusion'''
# 1. The most challenging part of the activity was keeing track of the variables because they were changed so much. We had a hard time with 
#    the part when having the turtle continue after the collision. The most enjoyable part was when the code worked like it was suppost to. 
 