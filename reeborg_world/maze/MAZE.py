# pyright: reportUndefinedVariable=false
# Reeborg's World - Maze
# This code only runs on Reeborg's World, not in normal Python.
# Try it here:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#These 3 lines are to avoid unnecessary loops in some exception cases
#------------------------------------
while front_is_clear():
    move()
turn_left()
#------------------------------------

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        