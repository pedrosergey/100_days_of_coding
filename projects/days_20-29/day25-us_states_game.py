# import some relevant libraries
import turtle

import pandas as pd
import turtle as t

# read the data that is in states

states = pd.read_csv("data/day25/day25_50-states.csv")

# get the list of states

states_list = states['state'].to_list()


# create the function to ask for a state

def check_answer(states_guessed):
    guessed_state = screen.textinput(f"{states_guessed}/50 States Correct", "What is another state name?")

    return guessed_state


# create a function that creates an object with and write the answer in the screen

def painter(state_guessed):
    x_guessed = states[states.state == state_guessed].x
    y_guessed = states[states.state == state_guessed].y
    state_turtle = t.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto(x=int(x_guessed), y=int(y_guessed))
    state_turtle.write(state_guessed, align="center")


# create and configure the screen of the game

screen = t.Screen()
screen.addshape("data/day25/day25_blankstatesimg.gif")
screen.title("States of the US")
turtle.shape("data/day25/day25_blankstatesimg.gif")
screen.setup(width=725, height=491)
screen.tracer(0)

# create the game

game_on = True
number_of_guesses = 0

while game_on:

    guess = check_answer(number_of_guesses).title()
    print(guess)

    if guess in states_list:
        painter(guess)
        screen.update()
        number_of_guesses += 1
        states_list.remove(guess)

    if number_of_guesses == 50 or guess.lower() == "off":
        game_on = False


remaining_states = pd.DataFrame(states_list)
remaining_states.to_csv("data/day25/need_to_learn.csv", header=["State"])
