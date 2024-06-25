# import some libraries
import turtle


class Paddle(turtle.Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.goto(x=x_cor, y=y_cor)
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        y_position = self.ycor()
        if y_position < 260:
            self.goto(x=self.xcor(), y=y_position + 20)

    def move_down(self):
        y_position = self.ycor()
        if -260 < y_position:
            self.goto(x=self.xcor(), y=y_position - 20)