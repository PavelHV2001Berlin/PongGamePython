from turtle import Turtle, Screen
from PlayerRacket import PlayerRacket
from Ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height = 600)

screen.title("Pong")
screen.tracer(0)

p1_racket = PlayerRacket(startingPosition=(-340,0))

p2_racket = PlayerRacket(startingPosition=(340,0))

ball = Ball(startingPosition=(0,0))

scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(p1_racket.up, "w")
screen.onkeypress(p1_racket.down, "s")

screen.onkeypress(p2_racket.up, "Up")
screen.onkeypress(p2_racket.down, "Down")

screen.update()


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    #detect paddle collision

    if ball.distance(p2_racket) < 50 and ball.xcor() > 320 or ball.distance(p1_racket) < 50 and ball.xcor() > -320:
        print("collision")
        ball.bounce_x()
    if ball.xcor() > 380:
        #punkt spieler 1
        scoreboard.increase_l_score()
        ball.reset_position()
    if ball.xcor() < -380:
        #punkt spieler 2
        scoreboard.increase_r_score()

        ball.reset_position()

    
