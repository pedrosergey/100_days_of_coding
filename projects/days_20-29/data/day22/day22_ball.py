# import some libraries

from turtle import Turtle
import random

BALL_SPEED = 0.075

# create the ball object

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("medium orchid")
        self.goto(0, 0)
        self.penup()
        self.start()
        self.ball_speed = BALL_SPEED

    def move(self):
        self.forward(10)

    def start(self):
        quadrant = random.randint(0, 3)

        if quadrant in [0, 2]:
            angle = random.randint(0 + quadrant * 90, 45 + quadrant * 90)
        else:
            angle = random.randint(quadrant * 90 + 45, 2 * quadrant * 90)

        self.setheading(angle)
        self.ball_speed = BALL_SPEED

    def bounce_wall(self):
        ball_angle = self.heading()
        self.setheading(360 - ball_angle)

    def bounce_paddle(self):
        ball_angle = self.heading()
        self.setheading((180 - ball_angle) % 360)
        self.ball_speed *= 0.9