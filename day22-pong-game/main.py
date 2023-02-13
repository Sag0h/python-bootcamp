from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Pong Game.")
screen.tracer(0)
screen.listen()

line = Turtle()
line.ht()
line.pd()
line.pencolor("white")
line.speed("fastest")
line.seth(270)
line.goto(0,300)
line.forward(600)
screen.update()

p1 = Paddle(-350, 0)
p2 = Paddle(350, 0)

screen.onkey(key="w",fun=p1.go_up)
screen.onkey(key="s",fun=p1.go_down)
screen.onkey(key="Up", fun=p2.go_up)
screen.onkey(key="Down", fun=p2.go_down)

sb = ScoreBoard()

ball = Ball()
ball.move()

game_is_on = True

ball_speed = 0.1
while(game_is_on):
    screen.update()
    ball.move()
    time.sleep(ball_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(p2) < 60) or (ball.xcor() < -320 and ball.distance(p1) < 60):
        ball.bounce_x()
        ball_speed *= 0.9


    if ball.xcor() > 400: 
        ball.reset()
        ball_speed = 0.1
        sb.increase_lscore()

    if ball.xcor() < -400:
        ball.reset()
        ball_speed = 0.1
        sb.increase_rscore()


screen.exitonclick()