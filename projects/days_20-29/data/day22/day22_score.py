# import some libraries
import turtle


class Score(turtle.Turtle):
    def __init__(self, x_cor, y_cor, special=False):
        super().__init__()
        self.hideturtle()
        self.goto(x=x_cor, y=y_cor)
        self.color("white")
        self.penup()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"{self.score}", move=False, align="center", font=('Courier', 58, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()