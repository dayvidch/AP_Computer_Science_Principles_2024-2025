import turtle as trtl
import random
import time

# initializing papple object
papple = trtl.Turtle()
papple.hideturtle()
papple_image = "pear.gif"
apple_image = "apple.gif"

# initializing variables
number_of_papples = 5
global score
global roundOver
roundOver = False
score = 0

# setting up the turtlescreen
wn = trtl.Screen()
wn.setup(width=800, height=800)
wn.addshape(papple_image)
wn.addshape(apple_image)
wn.bgcolor("white")

''' 
Creating the number of papples
'''
def createListofPapples():
    list = []
    for i in range(0, 5):
        papple = trtl.Turtle()
        papple.hideturtle()
        list.append(papple)
    return list

''' 
Sets up the papples on the screen left to right
'''
def draw_papple():
    global stopKey
    stopKey = True
    for i in range(0, 5):
        papples[i].showturtle()
    xCoor = -175
    yCoor = 300
    for i in range(0, number_of_papples):
        active_papple = papples[i]
        active_papple.shape(papple_image)
        active_papple.penup()
        active_papple.goto(xCoor, yCoor)
        active_papple.pendown()
        xCoor += 60
    wn.update()

''' 
Function to drop the papple
'''
def dropPapple(letterIndex):
    xcor = papples[letterIndex].xcor()
    ycor = papples[letterIndex].ycor()
    while (ycor > -30):
        ycor -= 15
        papples[letterIndex].penup()
        papples[letterIndex].goto(xcor, ycor)
        papples[letterIndex].pendown()
    papples[letterIndex].hideturtle()
    papples[letterIndex].penup()
    papples[letterIndex].goto(-175 + (60 * letterIndex), 300)
    papples[letterIndex].pendown()
    papples[letterIndex].shape(papple_image)
    papples[letterIndex].showturtle()

# initializing a timer object
timer_turtle = trtl.Turtle()
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(150, 150)

# basket setup
basket = trtl.Turtle()
basket.hideturtle()
basket.penup()
wn = trtl.Screen()
basket_img = "basket.gif"
wn.addshape(basket_img)
basket.shape(basket_img)
basket.goto(0, -100)

''' 
Moving the basket
'''
def move_runner():
    basket.forward(10)

''' 
Directions for the basket
'''
def up():
    if (stopKey == False):
        basket.setheading(90)
        move_runner()

def down():
    if (stopKey == False):
        basket.setheading(270)
        move_runner()

def left():
    if (stopKey == False):
        basket.setheading(180)
        move_runner()

def right():
    if (stopKey == False):
        basket.setheading(0)
        move_runner()

wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")

# freezing the basket
stopKey = False

# setting up the counter
counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(50, 0)
counter_interval = 1000
font_setup = ("Arial", 20, "normal")
timer = 5

''' 
This is the countdown to catch each turtle. If the time is out, it will freeze the movement of the basket
'''
def countdown(pappleIndex):
    global stopKey
    global timer, timer_up
    global roundOver
    stopKey = False
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        stopKey = True
        dropPapple(pappleIndex)
        if basket.xcor() - 30 < papples[pappleIndex].xcor() < basket.xcor() + 30:
            global score
            score += 1
            score_writer.clear()
            score_writer.write("Score: " + str(score), font=font_setup)
            roundOverGame(True)
        else:
            roundOverGame(False)
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(lambda: countdown(pappleIndex), counter_interval)

# initializing the score object
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-160, 0)

wn.listen()

papples = createListofPapples()

''' 
Pick a random papple to turn into the target apple
'''
def pick_papple(papples):
    currentPappleIndex = random.randint(0, len(papples)-1)
    papples[currentPappleIndex].shape(apple_image)
    return currentPappleIndex

''' 
This is for when the user has caught the papple
'''
def roundOverGame(gameOver):
    if gameOver == True:
        global timer
        timer = 5
        game()
    if gameOver == False:
        wn.clearscreen()
        wn.bgpic("defeat.gif")
        score_writer.goto(-55, 75)
        score_writer.write("Final Score: " + str(score), font=font_setup)

''' 
Writes the new score, picks a papple, and counts down
'''
def game():
    global counter_interval
    counter_interval -= 10
    score_writer.write("Score: " + str(score), font=font_setup)
    basket.showturtle()
    currentPappleIndex = pick_papple(papples)
    countdown(currentPappleIndex)

#setting up the starting screen
countdownTime = 3
startButton = trtl.Turtle()
startButton.penup()
startButton_img = "startbutton.gif"
wn.addshape(startButton_img)
startButton.shape(startButton_img)

''' 
Starting screen function
'''
def startingScreen(x, y):
    global countdownTime
    font_setupStart = ("Arial", 50, "normal")
    startButton.hideturtle()
    countDown = trtl.Turtle()
    countDown.hideturtle()
    for x in range(countdownTime):
        countDown.write(countdownTime, font=font_setupStart)
        time.sleep(1)
        countDown.clear()
        countdownTime -= 1
    wn.bgcolor("gray")
    draw_papple()
    game()

#when the start button is clicked, it starts the game
startButton.onclick(startingScreen)

#keeps the screen from closing
wn.mainloop()

