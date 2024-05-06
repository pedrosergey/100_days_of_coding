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
pencil.speed(100)

# configure the pencil and the canvas

canvas.setup(450, 450)
turtle.colormode(255)

# get the colour from the image that we chose

color_palette = colorgram.extract("data/day18_colours.jpg", 8)


# create the function that will chose the colours

def choose_color(colours):
    random_colour = random.choice(colours)
    r = random_colour.rgb[0]
    g = random_colour.rgb[1]
    b = random_colour.rgb[2]

    rgb = (r, g, b)

    return (rgb)


# configure until where do we want to pain

max_x = canvas.window_width() / 2 - 15
max_y = canvas.window_height() / 2 - 30
min_x = -(canvas.window_width() / 2) + 25
min_y = -(canvas.window_height() / 2) + 30

# configure the painting

pencil.pensize(15)
pencil.penup()
pencil.goto(min_x, min_y)

# create loop to paint

keep_painting = True

while keep_painting:

    pencil.dot(20, choose_color(color_palette))

    pencil.fd(40)
    print(pencil.pos())

    if pencil.pos()[0] > max_x and pencil.pos()[1] > max_y:
        pencil.fd(50)
        keep_painting = False

    elif pencil.pos()[0] > max_x:
        min_y = min_y + 40
        pencil.goto(min_x, min_y)

canvas.exitonclick()
