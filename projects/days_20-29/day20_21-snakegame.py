# import the necessary libraries
import random
import random as r
from turtle import Screen, Turtle
import time

# create and configure the screen and the snake

screen = Screen()
screen.bgcolor("black")
screen.setup(height=750, width=750)
screen.title("The Snake 🐍")
screen.tracer(0)


def grow_snake_body(x_position):
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("white")
    segment.goto(x=x_position, y=0)

    return segment


snake_body = []

for i in range(0, 3):
    snake_body.append(grow_snake_body(i * -20))


def move():

    for segment in range(1, len(snake_body)):
        previous_segment_position = snake_body[segment - 1].position()
        snake_body[segment].goto((previous_segment_position[0], previous_segment_position[1]))

    snake_body[0].forward(20)


def turn_right():
    facing = snake_body[0].heading()
    snake_body[0].setheading(facing - 90)


def turn_left():
    facing = snake_body[0].heading()
    snake_body[0].setheading(facing + 90)


screen.listen()

screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")


#TODO: put some food on the screen

# we need check where the snake is located to not put food in those locations

def create_food(snake_body_food):
    position_of_the_body = []
    possible_xy = range(-360, 360, 20)

    random_position = (float(random.choice(possible_xy)), float(random.choice(possible_xy)))

    for part_of_the_body in snake_body_food:
        position_of_the_body.append(part_of_the_body.position())

    if random_position in position_of_the_body:
        create_food(snake_body_food)
    else:
        food = Turtle(shape="circle")
        food.penup()
        food.color("lightblue")
        food.goto(x= random_position[0], y= random_position[1])
        return food


# def eat_food(snake_body_to_eat, food_to_eat):
#
#     if snake_body_to_eat[0].position() == food_to_eat.position():
#         snake_body_to_eat.append(snake_body_to_eat[-1])
#         food_to_eat.
#         snake_body_to_eat, False



#TODO: create a score board

#TODO: colission with the board

#TODO: colission with the snake

game_on = True
there_is_food = False

while game_on:
    move()
    time.sleep(0.2)
    screen.update()

    if not there_is_food:
        food = create_food(snake_body)
        there_is_food = True
    print(food.position(), snake_body[0].position())
    if food.position() == snake_body[0].position():
        there_is_food = False
        food.goto((700.0, 700.0))

screen.exitonclick()
