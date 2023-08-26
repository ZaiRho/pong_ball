from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.position = position
        self.refresh(position)

    def refresh(self, position):
        self.reset()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"{self.score}", True, "center", ("courier", 40, "normal"))

    def add_score(self):
        self.score += 1
        self.refresh(self.position)