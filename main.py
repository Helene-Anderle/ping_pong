from turtle import Screen, Turtle
from pong import Pong
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 800, height = 600)

screen.bgcolor("black")
screen.title("Helene's Ping Pong Game")
screen.tracer(0)

r_pong = Pong((350, 0))
l_pong = Pong((-350,0))
ball = Ball((0,0))
r_scoreboard = Scoreboard((150, 200))
l_scoreboard = Scoreboard((-150, 200))

screen.listen()
screen.onkey(r_pong.up, "Up")
screen.onkey(r_pong.down, "Down")
screen.onkey(l_pong.up, "w")
screen.onkey(l_pong.down, "s")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #Detect collision with wall
    if  ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect colission with r_padel
    if ball.distance(r_pong) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        r_scoreboard.increase_score()

    if ball.distance(l_pong) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        l_scoreboard.increase_score()

    #Right side padel miss
    if ball.xcor() > 400:
        ball.reset()
        l_scoreboard.increase_score()

    #Left side padel miss
    if ball.xcor() < -400:
        ball.reset()
        r_scoreboard.increase_score()

    if l_scoreboard.score == 10:
        l_scoreboard.l_win()
        game_is_on= False

    if r_scoreboard.score == 10:
        r_scoreboard.r_win()
        game_is_on = False

screen.exitonclick()