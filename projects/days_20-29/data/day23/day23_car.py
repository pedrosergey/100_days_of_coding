from turtle import Turtle
import random as r

COLORS = [color/255 for color in range(255)]
VELOCITY = 7

class CarsList():

    def __init__(self):
        self.cars = []
        self.movement = VELOCITY

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.color("black", (r.choice(COLORS), r.choice(COLORS), r.choice(COLORS)))
        car.penup()
        car.shapesize(stretch_wid=1.2, stretch_len=2.3)
        random_y = r.randint(-260, 260)
        car.goto(400, random_y)
        car.movement = self.movement

        self.cars.append(car)

    def increase_speed(self):
        self.movement *= 1.45

    def move(self):
        for car in self.cars:
            car.backward(self.movement)