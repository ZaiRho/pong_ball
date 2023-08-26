MOVE_STEP =50
from turtle import Turtle

class Player(Turtle):
    def __init__(self, coor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(coor)
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + MOVE_STEP)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - MOVE_STEP)
