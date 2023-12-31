from turtle import Turtle
import random
DIRECTION = [45,135,225,315]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh()

    def bounce(self):
        self.forward(20)
        if self.heading() == 45 and self.ycor() >= 280:
            self.seth(315)
        elif self.heading() == 135 and self.ycor() >= 280:
            self.seth(225)
        elif self.heading() == 225 and self.ycor() <= -280:
            self.seth(135)
        elif self.heading() == 315 and self.ycor() <= -280:
            self.seth(45)

    def player_bounce(self):
        if self.xcor() >350 or self.xcor() < -350:
            pass
        elif self.heading() == 45:
            self.seth(135)
        elif self.heading() == 135:
            self.seth(45)
        elif self.heading() == 225:
            self.seth(315)
        elif self.heading() == 315:
            self.seth(225)

    def refresh(self):
        self.reset()
        self.penup()
        self.shape("circle")
        self.color("coral")
        self.seth(random.choice(DIRECTION))