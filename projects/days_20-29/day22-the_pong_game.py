# import some libraries

from turtle import Screen, Turtle
from data.day22.day22_paddle import Paddle
from data.day22.day22_ball import Ball
from data.day22.day22_score import Score
import time

# create and configure the main screen

screen = Screen()
screen.setup(width=800, height=600)
screen.title("The PONG game!")
screen.bgcolor("black")
screen.tracer(0)

# create the middle of the field

middle = Turtle()
middle.penup()
dash_distance = round(600 / 40)
middle.goto(x=0, y=-300)
middle.color("white")
middle.setheading(90)
middle.hideturtle()
middle.pensize(5)

for _ in range(41):
    middle.pendown()
    middle.forward(dash_distance)
    middle.penup()
    middle.forward(dash_distance)

# create the paddles and the score board

r_paddle = Paddle(x_cor=350, y_cor=0)
l_paddle = Paddle(x_cor=-350, y_cor=0)

r_scorer = Score(x_cor=50, y_cor=200)
l_scorer = Score(x_cor=-50, y_cor=200)

ball = Ball()

# make the screen listen to events

screen.listen()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# configure the final state of the game

refresh_rate = 0.075
game_on = True

while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    if not -280 < ball.ycor() < 280:
        ball.bounce_wall()
        ball.forward(10)

    if (ball.distance(r_paddle) < 50 and 340 < ball.xcor()) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_paddle()
        ball.forward(10)

    if 390 < ball.xcor():
        time.sleep(refresh_rate)
        ball.start()
        ball.goto(0,0)
        l_scorer.increase_score()

    elif ball.xcor() < - 390:
        time.sleep(refresh_rate)
        ball.start()
        ball.goto(0,0)
        r_scorer.increase_score()


screen.exitonclick()
