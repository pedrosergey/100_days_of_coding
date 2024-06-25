# import the necessary libraries

import random
from turtle import Screen, Turtle
from data.day20.day20_snakeclass import Snake
from data.day20.day20_food import Food
from data.day20.day20_scoreboard import ScoreBoard
import time


# open and read the max score record

with open("data/day20/max_score.txt", mode="r") as f:
    record = int(f.read())


# create and configure the screen, and the snake

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("The Snake 🐍")
screen.tracer(0)

# initialize the objects

snake = Snake()
food = Food()
score = ScoreBoard()

# set up the historic record

if score.max_score < record:
    score.max_score = record

score.reset()

# make the screen listen to keystrokes

screen.listen()

screen.onkey(snake.turn_right, "d")
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_up, "w")
screen.onkey(snake.turn_down, "s")


# create a function to resume the game




# finishing the game

game_on = True

while game_on:

    screen.update()
    time.sleep(0.075)
    snake.move()

    if snake.snake_head.distance(food) < 10:
        food.move_food()
        score.add_score()
        snake.grow_body()

    if (not (-300 < snake.snake_head.xcor() < 290)) or (not (-300 < snake.snake_head.ycor() < 300)):
        score.reset()
        snake.reset()
        if score.max_score > record:
            with open("data/day20/max_score.txt", mode="w") as f:
                f.write(str(score.max_score))

    for part in snake.body[1:]:
        if snake.snake_head.distance(part) == 0:
            score.reset()
            snake.reset()
            if score.max_score > record:
                with open("data/day20/max_score.txt", mode="w") as f:
                    f.write(str(score.max_score))


screen.exitonclick()
