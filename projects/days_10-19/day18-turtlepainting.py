# in today's project, we are going to create an dot art, that I hope can be sold for millions
# as an example, we can see this kind of contemporaneous art from Damien Hirst

# import some libraries

from turtle import Turtle, Screen
import turtle
import random
import colorgram

# create the pencil and the canvas objects

pencil = Turtle()
canvas = Screen()

# configure the pencil and the canvas

canvas.screensize(350, 350)


turtle.colormode(255)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    rgb = (r, g, b)

    return rgb



# configure the screen to exit on click

canvas.exitonclick()
