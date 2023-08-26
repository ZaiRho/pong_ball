from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from ball import Ball

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)

player_1 = Player((350,0))
player_2 = Player((-350,0))
player1_score = Scoreboard((20,250))
ball = Ball()

screen.update()

screen.listen()
screen.onkey(player_1.move_up, "Up")
screen.onkey(player_1.move_down, "Down")
screen.onkey(player_2.move_up, "w")
screen.onkey(player_2.move_down, "s")

game_over = False

while not game_over:
    ball.bounce()
    if player_1.distance(ball.pos()) <= 40 and ball.xcor() >= 330:
        ball.player_bounce()
    if player_2.distance(ball.pos()) <= 40 and ball.xcor() <= -330:
        ball.player_bounce()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()