from turtle import Turtle

class Score(Turtle):

    def __init__(self, game_over = False):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        if game_over:
            self.write("GAME OVER", move=False, align="center", font=("Futura", 40, "normal"))
            self.goto(0, 0)
        else:
            self.goto(-210, 275)
            self.write(f"Level: {self.level}", move=False, align="center", font=("Futura", 40, "normal"))

    def move(self):
        self.forward(7)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", move=False, align="center", font=("Futura", 40, "normal"))

