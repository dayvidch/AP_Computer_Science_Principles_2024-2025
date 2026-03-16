'''Conditionals & The if statement'''
# 1. Prediction: 

'''
1. If the user inputs an integer or float greater than 90, the print statement would be activated. 
2. If the user input is less than 90, nothing would happen.
'''


# 2. Did the program work exactly like you thought it would? 

'''Yes, when the user input a number greater than 90 the print statement was outputted to the terminal. 
   However, when the input was less than 90, nothing occured since there was nothing to be executed.
'''

# 3

#Prediction
'''
1. If the user input a value 90 or greater, the code would execute the print statement "Input is 90 or more" onto the terminal.
2. If the user input a value less than 90, the code would execute the print statement "Input is less than 90".
'''

#Output
'''
Yes my prediction was correct, if the user input a value 90 or greater, 
the code would execute the print statement "Input is 90 or more" onto the terminal.
If the user input a value less than 90, the code would execute the print statement "Input is less than 90".
'''

'''Nested Conditionals''' 
# 4.

#Prediction
'''
1. The code would execute the print statements because the input would pass the first conditional statement as true, 
2. The second condition would be triggered 
3. Processed by the 2nd conditional statement which would also evaluate the statement as true.
4. The print statement would be output onto the terminal.
'''

#Output
'''
My prediction was correct, the code executed the print statement and output "You may graduate!" onto the terminal.
'''


# 5.
'''
year = int(input("Enter your year in school -> "))
if (year == 12):
  num_score = int(input("Enter your final score -> "))
  if (num_score >= 60):
    print("You may graduate!")

#Added code segment:
  else:
    print('Summer School?')
'''

# 6. 

#Prediction
'''
1. The user inputs a value that passes the first conditional statement 
2. The second input fufils the conditional statement
prints "You may graduate!"
                      or
2.The second input fails to fufil the second conditional statement
3.The user would be prompt a question
4. If the input fufils the condition 
5. The print statement stating "You may graduate!" would be executed.
        or
6. If the input doesn't fufil the condition
7. The print statement stating "Summer School?" would be executed.
'''

#Output
'''
Yes, my prediction was correct, if the user inputs 12 they pass the first condition and proceeds to the second condition.
If the user input fufils the second condition, they reach the end of the program and executes the print statement. However, 
if the second condition is not fufiled, then the program executes the third condition. If the value passes as fufiled, the print 
statement "You may graduate!" is printed onto the terminal. However, if the value is passed as false, the print statement
"Summer School?" would be executed.

'''


# 7.

#Predicton
'''
1. The user inputs a value 90 or greater
2. Print statement "Input is 90 or more" is executed
3. End of the Loop
               or
1. The user inputs a value less than 90
2. Program checks if the value fufills the second condition, if true, the print statement from the second condition is executd
                or
3. The user inputs a value less than 80
4. The Program checks if the value fufills the third condition, if true, the print statement from the third condition is executed
                or
5. The user inputs a value less than 70
6. The program checks if the value fufills the forth condition, if true, the print statement from the forth condition is executed
                or
7. The user inputs a value less than 60
8. The program executes the print statement from the else statement.

               
'''

#Output

'''
Yes, my prediction was correct, the terminal showcased the different outputs based on which conditional statement was fufiled. 
'''


 
'''The elif Statement'''
# 8 & 9.

#8
'''
Despite both programs achieving the same goal in producing different outputs based on the different conditional statements
being fufilled, the code on step 8 reduces the amount of syntax and complexity compared to the previous step. This makes
it easier for the programmer and their peers to understand the code and reduce confusion.
'''

#9
#Made code that it's easier to get a higher grade
#Changed int value to float so that students have a higher chance in getting a higher letter grade
'''
num = float(input("Enter a number -> "))
if (num >= 89.5):
  print("A")
elif (num >= 79.5):
  print("B")
elif (num >= 69.5):
  print("C")
elif (num >= 59.5):
  print("D")
else:
  print("F")
'''


# 10 & 11.

#10 Prediction
'''
1. The user inputs any value greater than 60
2. The first condition is fufilled
3. The first condition's body is executed
4. "D" is printed onto the terminal
5. End of the program
'''

#11
'''
Yes, I predicted the correct results as any value above 60 being input results in
the output of the string "D".
'''



'''College Board'''

'''Nested for loop Iteration'''
# 12-14. 
# Prediction:

'''
1. The Program would iterate through the first item in the "days_of_week",
2. The program would iterate through each of the items in the "my_courses" list
3. The program would continue iterating the 1st "for loop" for the remaining amount
  of items in the list "days_of_week"
4. Each of the item from the "days_of_week" would be be accompanied by 
   each of the items from the "my_courses" list
'''


# Did the program work exactly like you thought it would? 

'''
Yes, the program iterated through each of the "days_of_week" items, and each item
is accopanied by the items from the "my_courses" list.
'''

# 14
'''
1. 5 Iterations occured in the Outer Loop,
2. 3 Iterations occured in the inner loop each time the outerloop iterated
3. Total of 15 iterations
''' 




'''Nested Loops and Conditionals'''

# 15 through 17. Program & Test your code for a couple examples in the terminal then summerize your results: 

#   a118_grades.py
#   This code is incomplete. 
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
#Summarize:
'''
1. For each subject, the user inputs a grade
2. Based on the input, a different conditional statement gets executed
3. After the conditional statement gets executed, the user is prompt whether or not
they want to input their grade again.
4. If the answer is false, the program would continue to iterate the "for loop" for
each item in the "my_courses" list
'''



'''Turtles Stop!'''
# 18 through 20 use the code below (made changes from the original so it would fit in replt.

# # a118_turtles_in_traffic.py
# # Move turtles horizontally and vertically across screen.
# # Stopping turtles when they collide.
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
  #Sets the turtle's shape in the horizonta row to each item in "turtle_shapes, and sets the turtle's color to each color in the "horiz_colors"
  ht = trtl.Turtle(shape=s)
  ht.turtlesize(.5)
  #ht.speed(2)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-115, tloc)
  ht.setheading(0)
  #Sets the turtle's shape in the vertical column to each item in the "turtle_shapes", and sets the turtle's color to each color in the "vert_colors"
  vt = trtl.Turtle(shape=s)
  vt.turtlesize(.5)
  #vt.speed(2)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 115)
  vt.setheading(270)
  #Increments the variable to make the turtle travel 35 units from its last location
  tloc += 35

# TODO: move turtles across and down screen, stopping for collisions
vt.speed(5)

print(horiz_turtles)

for step in range(80):
  
  for ht in (horiz_turtles):
    ht.speed(speed)
    ht.forward(5)
  
  for vt in (vert_turtles):
    vt.speed(speed)
    vt.forward(5)
    if(abs(ht.xcor() - vt.xcor()) < 10):
        vert_turtles.remove(vt)
        horiz_turtles.remove(ht)
  
wn = trtl.Screen()
wn.mainloop()
'''

'''It’s Your Turn'''

'''
The following code draws turtle objects at random shapes and colors each time the program is runned. Additionally, whenever the turtles collide, each separate iteration brings a different
animation before the turtles goes back to its original route.
'''

# 21 through 22 copy and paste the completed code from the above section and make all the modifications you can.
import turtle as trtl
import time as time
import random

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

colors = ["red", "blue", "green", "orange", "purple", "gold", "darkred", "darkblue", "lime", "salmon", "indigo", "brown", "gray"]
rand_shape = []
for item in turtle_shapes:
  ran = random.randint(0, len(turtle_shapes)-1)
  rand_shape.append(turtle_shapes[ran])

tloc = -95
for s in rand_shape:
  #Sets the turtle's shape in the horizonta row to each item in "turtle_shapes, and sets the turtle's color to each color in the "horiz_colors"
  ht = trtl.Turtle(shape=s)
  ht.turtlesize(.5)
  #ht.speed(2)
  horiz_turtles.append(ht)
  ht.penup()
  for item in horiz_colors:
    random_color = []
    random_color0 = random.randint(0, len(horiz_colors)-1)
    random_color.append(horiz_colors[random_color0])
  
  new_color = random_color.pop()
  ht.fillcolor(new_color)
  ht.goto(-115, tloc)
  ht.setheading(0)
  #Sets the turtle's shape in the vertical column to each item in the "turtle_shapes", and sets the turtle's color to each color in the "vert_colors"
  vt = trtl.Turtle(shape=s)
  vt.turtlesize(.5)
  #vt.speed(2)
  vert_turtles.append(vt)
  vt.penup()
  for item in vert_colors:
    random_color = []
    random_color0 = random.randint(0, len(vert_colors)-1)
    random_color.append(vert_colors[random_color0])
  
  new_color = random_color.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 115)
  vt.setheading(270)
  #Increments the variable to make the turtle travel 35 units from its last location
  tloc += 35

# TODO: move turtles across and down screen, stopping for collisions
vt.speed(5)

#Makes a for loop which is responsible for all of the turtle's traffic after the turtles are brought to their original locations
for step in range(45):

  #Sets "ht" as each item in horizontal turtles list
  for ht in (horiz_turtles):
    
    #Randomizes the speed from 0 to 10. 
    ht.speed(random.randint(0,10))
    #Moves the horizontal turtles forward by 5.
    ht.forward(5)
  
  #Sets "vt" as each item in vertical turtles list
  for vt in (vert_turtles):
    vt.forward(5)
    vt.turtlesize(0.5)
    #Saves the turtle's color and shape so after the collision animation, the turtle's could regain their former appearance and properties. 
    og_shape = vt.shape()
    og_color = vt.color()
    act_color = og_color[1]
    vt.speed(random.randint(0,10))
    
    for ht in horiz_turtles:
      #Detects whether or not the turtles has collided with one another
      if(abs(ht.xcor() - vt.xcor()) < 10 and abs(ht.ycor() - vt.ycor() < 10)):
        #For 4 times, the turtle that has collided would change shape and color randomly

        vt.turtlesize(1)
        #Using randint from the random library, we were able to randomize the shape and color
        random_shape = random.choice(turtle_shapes)
        random_color = random.choice(colors)
        vt.begin_fill()
        vt.fillcolor(random_color)
        vt.shape(random_shape)
        vt.end_fill()
        time.sleep(0.1)
        vt.turtlesize(0.5)
        vt.begin_fill()
        print(og_color)
        vt.fillcolor(act_color)
        vt.shape(og_shape)
        vt.end_fill()
        
        #Makes the collided turtles head backwards and continue their route
        vt.speed(random.randint(0,10))
        vt.forward(-15)
        ht.forward(10)
        vt.setheading(270)
        break

#Keeps the terminal on even after everything is run
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

# Quiz:

# 3 out of 3

# Skip AP review section
 
'''
Conclusion
'''
# 1. 
'''The most enjoyable part was seeing some part of the program work. 
The most challenging part of the activity was creating the nested loops as the codes became much harder to debug. 
'''
#Displaying LastFirst_LastFirst_1.1.8.py.