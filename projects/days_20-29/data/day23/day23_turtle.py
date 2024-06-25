from turtle import Turtle

class CrossingTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red", "lime green")
        self.penup()
        self.start_position()
        self.setheading(90)
        self.shapesize(1.5)

    def move(self):
        self.forward(7)

    def start_position(self):
        self.goto(0, -285)
