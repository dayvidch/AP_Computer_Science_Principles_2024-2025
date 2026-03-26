import turtle as trtl
import time

wn = trtl.Screen()
painter = trtl.Turtle()


def timer():
    timer = 0
    while True:
        painter.write(timer, font = ("Futura", 60, "normal"))
        time.sleep(1)
        timer += 1
        painter.clear()

timer()


wn.mainloop()