from turtle import Turtle

MOVE_DISTANCE = 20
SNAKE_BODY_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake(SNAKE_BODY_POSITION)
        self.snake_head = self.body[0]

    def create_snake(self, segments):
        for segment in segments:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(segment)
            self.body.append(new_segment)

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            previous_segment_position = self.body[segment - 1].position()
            self.body[segment].goto((previous_segment_position[0], previous_segment_position[1]))

        self.snake_head.forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.body:
            segment.goto(500,500)
        self.body.clear()
        self.create_snake(SNAKE_BODY_POSITION)
        self.snake_head = self.body[0]

    def grow_body(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.body[-1].position())
        self.body.append(new_segment)

    def turn_right(self):
        facing = self.snake_head.heading()
        if facing != LEFT:
            self.snake_head.setheading(RIGHT)

    def turn_left(self):
        facing = self.snake_head.heading()
        if facing != RIGHT:
            self.snake_head.setheading(LEFT)

    def turn_up(self):
        facing = self.snake_head.heading()
        if facing != DOWN:
            self.snake_head.setheading(UP)

    def turn_down(self):
        facing = self.snake_head.heading()
        if facing != UP:
            self.snake_head.setheading(DOWN)
