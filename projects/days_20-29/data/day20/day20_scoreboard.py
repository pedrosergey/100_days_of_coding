from turtle import Turtle
import random

possible_points = range(-280, 281, 20)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.max_score = 0
        self.goto(x=0, y=275)
        self.write_score()
    def write_score(self):
        self.clear()
        self.write(f"Score:   {self.score} | High Score:  {self.max_score}", move=False, align="center",
                   font=('Arial', 18, 'normal'))
    def add_score(self):
        self.score += 1
        if self.score > self.max_score:
            self.max_score = self.score
        self.write_score()
    def reset(self):
        if self.score > self.max_score:
            self.max_score = self.score
        self.score = 0
        self.write_score()


