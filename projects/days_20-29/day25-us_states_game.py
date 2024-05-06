# import some relevant libraries

import pandas as pd
import turtle as t

# read the data that is in states

states = pd.read_csv("data/50_states.csv")

# create the function to ask for a state

def check_answer(states_guessed):
    guess = screen.textinput(f"{states_guessed}/50 States Correct", "What is another state name?")

# create a function that creates an object with and write the answer in the screen

def painter(state_guessed):
    x_guessed = states[states.state == state_guessed].x
    y_guessed = states[states.state == state_guessed].y
    state_turtle = t.Turtle()
    state_turtle.goto(x_guessed, y_guessed)

# create and configure the screen of the game

screen = t.Screen()
screen.bgpic("data/blank_states_img.gif")
screen.title("States of the US")
screen.setup(width= 725, height= 491)

screen.exitonclick()



