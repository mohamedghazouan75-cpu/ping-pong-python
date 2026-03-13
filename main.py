from turtle import Screen
from paddles import Paddle
from scorebord import Scorbord
from ball import Ball
import time
screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('Ping Pong by Ghazouan')
screen.tracer(0)

# creat player1:
player1 = Paddle((350,0))
player1.color('blue')
# creat player2:
player2 = Paddle((-350,0))
# creat lin in the midle:
line = Paddle((0,0))
line.shapesize(25,.1)
line.color("white")
# creat the scor
scor = Scorbord((0,260))
# creat the ball
ball = Ball((0,0))
screen.listen()
screen.onkey(player1.up,'Up')
screen.onkey(player1.down,'Down')
ttime =0.09

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ttime)
    # تحريك الكره
    ball.goto(ball.xcor()+ball.dx,ball.ycor()+ball.dy) 
    # في حاله لمس الحائط العلوي او السفلي
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.dy *= -1
    # في حاله لمس الكره للمضرب الايمن
    if (ball.xcor() >= 330  and ball.distance(player1) <= 55):
        ball.dx *= -1
        scor.add_score1()
        ttime -= 0.003
    # في حاله لمس الكره للمضرب الايسر
    if (ball.xcor() <= -330 and ball.distance(player2) <= 55):
        ball.dx *= -1
        scor.add_score2()
        ttime -= 0.003
    # تحريك اللاعب الايسر اوتوماتيكيا
    if ball.dx<0 :
       player2.goto(player2.xcor(),ball.ycor())
    # اذا خرجت الكره خارج المدار
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        ttime = 0.06
         
        
screen.exitonclick()