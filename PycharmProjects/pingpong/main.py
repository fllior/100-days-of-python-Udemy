from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    #if the ball hits the length wall other player gets a point
    # if ball.xcor() < -280 or ball.ycor() > 280:
    #     game_is_on = False
    #     print("Game over")
    #     print(ball.xcor(), ball.ycor())
    #     #score.game_over()

    if ball.ycor() > 280 or ball.ycor() < -280:
        print("bounce back")
        print(ball.xcor(), ball.ycor())
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        #ball.increase_speed()
        #print(ball.)



    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
screen.update()








screen.exitonclick()