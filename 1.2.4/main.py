import turtle as trtl

#Question 3
'''
#setup 
wn = trtl.Screen()

#Maze setup
maze_painter = trtl.Turtle()
maze_painter.hideturtle()
maze_painter.pensize(3)
maze_painter.speed(0)

side_lenght = 20

for x in range(20):
    side_lenght += 20
    for x in range(2):
        maze_painter.forward(side_lenght)
        maze_painter.right(90)

#function calls
wn.mainloop()
'''

#Question 7
'''
#setup 
wn = trtl.Screen()

#Maze setup
maze_painter = trtl.Turtle()
maze_painter.hideturtle()
maze_painter.pensize(3)
maze_painter.speed(0)

side_lenght = 10
door_lenght = 20
for x in range(20):
    side_lenght += 20
    for x in range(2):
        maze_painter.forward(side_lenght/2)
        maze_painter.penup()
        maze_painter.forward(door_lenght)
        maze_painter.pendown()
        maze_painter.forward(side_lenght/2)
        maze_painter.right(90)

#function calls
wn.mainloop()
'''

#Question 11
'''
import turtle as trtl

#setup 
wn = trtl.Screen()

#Maze setup
maze_painter = trtl.Turtle()
maze_painter.hideturtle()
maze_painter.pensize(3)
maze_painter.speed(0)

side_length = 10
door_length = 20
barrier_length = 25

for x in range(20):
    if x in range(4):
        maze_painter.penup()
    else:
        maze_painter.pendown()
        side_length += 20
        for x in range(2):
            maze_painter.forward(side_length/2)
            #door
            maze_painter.penup()
            maze_painter.forward(door_length)
            maze_painter.pendown()
            maze_painter.forward(side_length/2)
            #Barriers
            maze_painter.back(side_length/4)
            maze_painter.right(90)
            maze_painter.forward(barrier_length)
            maze_painter.back(barrier_length)
            maze_painter.left(90)

            maze_painter.forward(side_length/2)
            maze_painter.right(90)
'''

#Question 16
'''
import turtle as trtl
import random as rand

#setup 
wn = trtl.Screen()

#Maze setup
maze_painter = trtl.Turtle()
maze_painter.hideturtle()
maze_painter.pensize(3)
maze_painter.speed(0)

side_length = 10
door_length = 20
barrier_length = 20

#Drawing the maze
for x in range(20):
    if x in range(3):
        maze_painter.penup()
    else:
        maze_painter.pendown()

        for x in range(2):
            total_side_length = side_length/2
            first_half = rand.randrange(int(total_side_length))
            second_half = total_side_length - first_half
            maze_painter.forward(first_half)
            #Doors
            maze_painter.penup()
            maze_painter.forward(door_length)
            maze_painter.pendown()
            maze_painter.forward(second_half)
            #Barriers
            maze_painter.back(second_half)
            maze_painter.right(90)
            maze_painter.forward(barrier_length)
            maze_painter.back(barrier_length)
            maze_painter.left(90)
            maze_painter.forward(second_half)
            maze_painter.right(90)
            side_length += 20

#function calls
wn.mainloop()
'''

#Question 23
'''
import turtle as trtl
import random as rand

#functions
def draw_door():
    maze_painter.penup()
    maze_painter.forward(door_length)
    maze_painter.pendown()
    maze_painter.forward(second_half)

def draw_barrier():
    maze_painter.back(second_half)
    maze_painter.right(90)
    maze_painter.forward(barrier_length)
    maze_painter.back(barrier_length)
    maze_painter.left(90)
    maze_painter.forward(second_half)
    maze_painter.right(90)

#setup 
wn = trtl.Screen()

#Maze setup
maze_painter = trtl.Turtle()
maze_painter.hideturtle()
maze_painter.pensize(3)
maze_painter.speed(0)

side_length = 10
door_length = 20
barrier_length = 20

#Drawing the maze
for x in range(20):
    if x in range(3):
        maze_painter.penup()
    else:
        maze_painter.pendown()

        for x in range(2):
            total_side_length = side_length/2
            first_half = rand.randrange(int(total_side_length))
            second_half = total_side_length - first_half
            maze_painter.forward(first_half)

            #Doors
            draw_door()

            #Barriers
            draw_barrier()

            #Increment each side
            side_length += 20

#function calls
wn.mainloop()
'''

#Question 36
'''
Controls are wasd, and to move is the spacebar
'''

import turtle as trtl
import random as rand

#Maze functions
def draw_door():
    maze_painter.penup()
    maze_painter.forward(door_length)
    maze_painter.pendown()
    maze_painter.forward(second_half)

def draw_barrier():
    maze_painter.back(second_half)
    maze_painter.right(90)
    maze_painter.forward(barrier_length)
    maze_painter.back(barrier_length)
    maze_painter.left(90)
    maze_painter.forward(second_half)
    maze_painter.right(90)

#Runner functions

#directions
def up():
    Fortnite_runner.setheading(90)

def down():
    Fortnite_runner.setheading(270)

def left():
    Fortnite_runner.setheading(180)

def right():
    Fortnite_runner.setheading(0)

#moving
def move_runner():
  Fortnite_runner.forward(10)

#General setup 
wn = trtl.Screen()

#Maze setup
maze_painter = trtl.Turtle()
maze_painter.hideturtle()
maze_painter.pensize(3)
maze_painter.speed(0)

side_length = 10
door_length = 50
barrier_length = 50

#Drawing the maze
for x in range(20):
    if x in range(3):
        maze_painter.penup()
    else:
        maze_painter.pendown()

        for x in range(2):
            total_side_length = side_length/2
            first_half = rand.randrange(int(total_side_length))
            second_half = total_side_length - first_half
            maze_painter.forward(first_half)

            #Doors
            draw_door()

            #Barriers
            draw_barrier()

            #Increment each side
            side_length += 50

#Maze Runner Setup
Fortnite_runner = trtl.Turtle()
Fortnite_image = "medium.gif"
wn.addshape(Fortnite_image)
Fortnite_runner.shape(Fortnite_image)


#function calls

#directions
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")

#moving
wn.onkeypress(move_runner," ")

wn.listen()
wn.mainloop()


#Discussion Prompt Questions
# Question 1
    # Algorithms can be written in different ways and still accomplish the same task by having the main goal be the same.
    # Just like in math, you can move the variables around, but as long as your solving for the same thing, and both methods are correct,
    # they will end up with the same conclusion.

# Question 2
    #Algorithms that appear similar can yield different side effects / results because that means that the logic between those two algorithms
    #were different.

#Conclusion Questions
# Question 1
    # Pseudocode is useful because it helps you plan out all the details before coding, so it is alot easier to change things. Its easier to
    # read because it is all in english, and its easier to write for that same reason too.

# Question 2
    # The draw doors algorithm works by having the pen got up so it doesnt leave a trail, then comming back down after it had left a gap in the line.
    # The draw barriers works by having the maze painter change dirrectons perpendicular of the line, then going down then back up. It then 
    # continues drawing the rest of the maze. They both relate to each other because the intended burpose was to have a random maze, and inorder
    # for it to be random, they both need to work without overlapping each other.