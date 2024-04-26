# today's project consisted in develop a solution for the famous game Reeborg's World
# you can try the game by visiting: https://reeborg.ca/
# the final version of the code, that will save this little robot from every situation is:


def turn_right():
    turn_left()
    turn_left()
    turn_left()


turn_around = 0

while not at_goal():

    if right_is_clear() and turn_around < 4:
        turn_right()
        move()
        turn_around += 1

    elif front_is_clear():
        move()
        turn_around = 0

    else:
        while not front_is_clear():
            turn_left()
        move()
        turn_around = 0
