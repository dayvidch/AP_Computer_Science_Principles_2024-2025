import turtle as trtl
import time
wn = trtl.Screen()

countdownTime = 3

startButton = trtl.Turtle()
startButton.penup()
startButton_img = "startbutton.gif"
wn.addshape(startButton_img)
startButton.shape(startButton_img)

def startingScreen(x,y):
    global countdownTime
    font_setupStart = ("Arial", 50, "normal")
    wn.clear()
    countDown = trtl.Turtle()
    countDown.hideturtle()
    for x in range(countdownTime):
      countDown.write(countdownTime, font=font_setupStart)
      time.sleep(1)
      wn.clear()
      countdownTime -=1

startButton.onclick(startingScreen)


wn.listen()
wn.mainloop()