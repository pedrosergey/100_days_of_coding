# import the neccesary libraries

import random as r
from turtle import Screen, Turtle
import time

# create and configure the screen and the snake

screen = Screen()
screen.bgcolor("black")
screen.setup(height= 750, width= 750)
screen.title("The Snake 🐍")
screen.tracer(0)

def grow_snake_body(x_position):
    segment = Turtle(shape = "square")
    segment.penup()
    segment.color("white")
    segment.goto(x = x_position, y = 0)
    
    return segment

snake_body = []

for i in range(0,3):
    snake_body.append(grow_snake_body(i * -20))


#TODO: how to move the snake

def move():

    heading_position = snake_body[0].pos()
    
    snake_body[0].forward(20)
 
    for segment in range(1, len(snake_body)):

        previous_segment_position =  snake_body[segment - 1].position()
        snake_body[segment].position()


def turn_right():
    facing = snake_body[0].heading()
    snake_body[0].setheading(facing - 90) 

def turn_left():
    facing = snake_body[0].heading()
    snake_body[0].setheading(facing + 90)


screen.listen()

screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")


while True:
    for _ in range (3):
        move()
        time.sleep(0.2)
        screen.update()
    snake_body[0].setheading(90)
    move()
    time.sleep(0.2)
    screen.update()
    move()
    time.sleep(0.2)
    screen.update()



#TODO: move the sanke

#TODO: put some food on the screen

#TODO: create a score board

#TODO: colission with the board

#TODO: colission with the snake

screen.exitonclick()