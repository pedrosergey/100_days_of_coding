from turtle import Turtle
import random

possible_points = range(-280, 281, 20)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("chartreuse")
        self.shapesize(stretch_wid=.65, stretch_len=.65)
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        random_x = random.choice(possible_points)
        random_y = random.choice(possible_points)
        self.goto(random_x, random_y)
