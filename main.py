from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
#
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

on = True
while on:
    time.sleep(.1)
    screen.update()

    ball.move()
    #detect if ball hits the top or bottom wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    #detect if ball hits paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()

        scoreboard.right_score()
    if ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_paddle()

        scoreboard.left_score()

    #detect if loses
    if ball.xcor() > 400:
        scoreboard.game_over("Left")
        on = False
    elif ball.xcor() < -400:
        scoreboard.game_over("Right")
        on = False

screen.exitonclick()

