
from colorama import init, Style
import random
print("Welcome to the School Shooting Prevention Program!")
def cur():
    print(Style.BRIGHT + """
In the event of a school shooting, your first priority should be to stay safe 
by following the Run, Hide, Fight strategy.

If there is a clear and safe path to escape, run immediately—leave your belongings, 
encourage others to come with you, and keep your hands visible as you exit.

If escaping isn't possible, hide in a secure location. Lock and barricade doors, 
turn off lights, silence your phone, and stay quiet and out of sight.

As a last resort, if your life is in immediate danger and you have no other options, 
be prepared to fight. Use any available objects to disorient or stop the attacker, 
and work with others if possible.

Always follow your school's emergency procedures and wait for law enforcement 
instructions once you're safe.
""" + Style.RESET_ALL)

def prac():
    randomCase = random.randint(1, 5)
    if (randomCase == 1):
        print("""
Scenario 1:
You are in your computer science principles class. Suddenly, you are notified that 
there has been a school shooter on the other side of the school and is 1000 feet 
away from you currently. What would you do?
""")
        case = input("Run, hide, fight? (r, h, f)")
        if (case == "r"):
            print("Score: 3")
        elif (case == "h"):
            print ("Score: 2")
        elif (case == "f"):
            print ("Score: 1")
        else:
            print("Doing nothing is not going to save you. ")
            print("Score: 0")


    
    elif (randomCase == 2):
        
        print("""
        Scenario 2:
        You are in the gym during P.E. class when you hear loud popping sounds coming 
        from the science wing. A teacher yells that it might be gunfire and quickly 
        locks the doors. You can’t see the shooter, but the sounds seem to be getting louder. 
        What actions should you take?
        """)
        case = input("Run, hide, fight? (r, h, f)")
        if (case == "r"):
            print("Score: 1")
        elif (case == "h"):
            print ("Score: 3")
        elif (case == "f"):
            print ("Score: 2")
        else:
            print("Doing nothing is not going to save you. ")
            print("Score: 0")
    
    elif (randomCase == 3):
        print("""
Scenario 3:
You're in the library working on a group project. Suddenly, a lockdown announcement 
comes over the intercom, followed by screams in the hallway nearby. You hear running 
footsteps and someone bangs on the door. You don’t know if it’s a student or the shooter. 
How do you respond?
""")
        case = input("Run, hide, fight? (r, h, f)")
        if (case == "r"):
            print("Score: 1")
        elif (case == "h"):
            print ("Score: 3")
        elif (case == "f"):
            print ("Score: 2")
        else:
            print("Doing nothing is not going to save you. ")
            print("Score: 0")
    elif (randomCase == 4):
        print("""
Scenario 4:
You're walking back from the restroom when you hear "Code Red" over the intercom 
and students running toward you. You realize your classroom is on the opposite end 
of the building. You're alone in the hallway. What do you do next?
""")
        case = input("Run, hide, fight? (r, h, f)")
        if (case == "r"):
            print("Score: 2")
        elif (case == "h"):
            print ("Score: 1")
        elif (case == "f"):
            print ("Score: 3")
        else:
            print("Doing nothing is not going to save you. ")
            print("Score: 0")
    else:
        print("""
Scenario 5:
You're outside in the courtyard during lunch when students begin screaming and running 
in all directions. You hear someone yell that a shooter is inside the cafeteria. 
You’re about 200 feet away and not near any buildings. What’s your best course of action?
""")
        case = input("Run, hide, fight? (r, h, f)")
        if (case == "r"):
            print("Score: 3")
        elif (case == "h"):
            print ("Score: 1")
        elif (case == "f"):
            print ("Score: 2")
        else:
            print("Doing nothing is not going to save you. ")
            print("Score: 0")





while True:
    print(Style.RESET_ALL + "Would you like to learn more, practice decision making, or quit?")
    start = input("press one of the options(l, p, q)")
    if (start == "l"):
        cur()

    elif (start == "p"):
        prac()

    elif (start == "q"):
        print("Thank you for using our services. Terminating program. ")
        break
    else:
        print("Invalid input. Terminating program")
        break