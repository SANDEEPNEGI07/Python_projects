from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor('Black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.listen()
#movement for right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down" )

#movement for left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s" )

ball = Ball()
score = Score()

game_is_on = True
while game_is_on:
    time.sleep(ball.velo)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 45 and ball.xcor() > 330:
        ball.setx(330)
        ball.bounce_x()

    if ball.distance(l_paddle) < 45 and ball.xcor() < -330:
        ball.setx(-330)
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor() > 380:
        ball.ball_reset()
        score.l_point()
    #detect L paddle misses
    if ball.xcor() < -380:
        ball.ball_reset()
        score.r_point()

screen.exitonclick()