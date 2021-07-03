from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.screensize(canvwidth=800,canvheight=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
right_paddle = Paddle((350 , 0))
left_paddle =  Paddle((-350,0))
ball = Ball()
screen.update()
player1_score= ScoreBoard("Player 1", (-200,260))
player2_score= ScoreBoard("Player 2", (200,260))


screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

game_on = True
while game_on:
    screen.update()
    ball.move(left_paddle,right_paddle)
    if not ball.in_bounds():
        if ball.xcor()<0 :
            player2_score.increase_score()
        else:
            player1_score.increase_score()
        time.sleep(1)
        ball.goto((0,0))
    if player1_score.score == 5 or player2_score.score == 5:
        game_on=False
        ScoreBoard("GAME OVER!",(0,0))

    time.sleep(0.00001)


screen.exitonclick()