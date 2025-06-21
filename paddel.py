from turtle import Turtle
class Paddel(Turtle):
          def __init__(self,postion):
                  super().__init__()
                  self.shape("square")
                  self.color("white")
                  self.penup()
                  self.shapesize(5,1)
                  self.goto(postion)
          def go_up(self):
                  self.goto(self.xcor(),self.ycor()+40)
          def go_down(self):
                  self.goto(self.xcor(),self.ycor()-40)                 