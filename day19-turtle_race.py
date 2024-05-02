# import some libraries

from turtle import Screen, Turtle
import random as r

# create and configure the screen

screen = Screen()
screen.setup(height= 400, width= 500)

# ask the user to bet for a winner

user_bet = screen.textinput(title = "Make your bet!", prompt= "Choose the color of the turtle that you think is going to win!").lower()

# create a variable to start the race

race_on = False

# create the turtles and move it to the starting line

colours = ['red','purple','yellow','orange','blue', 'lightblue','green']
positions = [141, 94, 47, 0, -47, -94, -141]
turtles = {}


for color in range(0, len(colours)):

    name = f"turtle_{colours[color]}"

    turtles[name] = Turtle(shape= "turtle")
    turtles[name].shapesize(2,2,1)
    turtles[name].color(colours[color])
    turtles[name].penup()
    turtles[name].goto(x= -220, y= positions[color])


# configure the race to start when the user has introduce its bet

if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:
        random_distance = r.randint(0, 15)
        turtles[turtle].forward(random_distance)

        if turtles[turtle].xcor() > 210.0:
            winner_color = turtles[turtle].pencolor()
            race_on = False

screen.exitonclick()

if user_bet == winner_color:
    print(f"Congratulations, the {user_bet} turtle won the race!")
else:
    print(f"Bad luck. You chose the {user_bet} turtle and the {winner_color} turtle won.")
