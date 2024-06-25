# import some libraries
import time
import turtle
from turtle import Screen
import random as r
from data.day23.day23_turtle import CrossingTurtle
from data.day23.day23_car import CarsList
from data.day23.day23_score import Score

# create some global variables

FINISH_LINE = 275

# create and set the screen

screen = Screen()

screen.screensize(600, 600)
screen.bgcolor("white")
screen.title("The Turtle game 🐢🚗")
screen.listen()
screen.tracer(0)

# create and configure the turtle and the cars

crossing_turtle = CrossingTurtle()

screen.onkey(crossing_turtle.move, "w")

# TODO 4: Add the scoreboard and speed up

game_on = True
counter = 0

generated_cars = CarsList()
generated_cars.create_car()
level = Score()

while game_on:
    screen.update()
    time.sleep(0.07)

    if counter % 5 == 0:
        generated_cars.create_car()

    generated_cars.move()

    if FINISH_LINE < crossing_turtle.ycor():
        crossing_turtle.start_position()
        generated_cars.increase_speed()
        level.increase_level()

    for car in generated_cars.cars:
        if car.distance(crossing_turtle) < 20:
            game_on = False
            game_over = Score(game_over=True)









    counter += 1

screen.exitonclick()