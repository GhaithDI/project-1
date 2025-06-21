from turtle import Screen,Turtle
from paddel import Paddel
from ball import Ball
from score import Score_bord
import time
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("OctuCode:Pingpong")
screen.tracer(0)
 
r_paddel=Paddel((350,0))
l_paddel=Paddel((-350,0))
ball=Ball()
r_score=Score_bord((250,270))
l_score=Score_bord((-250,270))

screen.listen()
screen.onkey(r_paddel.go_up,"Up")
screen.onkey(r_paddel.go_down,"Down")
screen.onkey(l_paddel.go_up,"w")
screen.onkey(l_paddel.go_down,"s")
time_sleep=0.1
game_on=True
while game_on:
          screen.update()
          time.sleep(time_sleep)
          ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)
          #اكتشاف التصادم مع السقف
          if ball.ycor() >=280 or ball.ycor()<=-280:
                  ball.y_move *=-1
          #اكتشاف التصادم مع المضارب
          if (ball.xcor()>=330 and ball.distance(r_paddel)<=50) or (ball.xcor()<-330 and ball.distance(l_paddel)<=50) :         
                  ball.x_move *=-1
                  time_sleep *=0.9
                
                 
                 
          #اكتشاف التصادم مع الحائط الايمن
          if ball.xcor() >430:
                  l_score.increase_score()
                 # ball.goto(0,0)
                  ball.x_move *=-1
                  time_sleep =0.1
                  l_score.game_over()
                  game_on=False
          #اكتشاف التصادم مع الحائط الايسر
          if ball.xcor() <-430:
                  r_score.increase_score()
                  #ball.goto(0,0)
                  ball.x_move *=-1
                  time_sleep = 0.1
                  r_score.game_over()
                  game_on=False
                   
                                 



screen.exitonclick()