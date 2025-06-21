from turtle import Turtle

class Score_bord(Turtle):
          def __init__(self,postion):
                  super().__init__()
                  self.score=0
                  self.high_score=0
                  self.shape("turtle")
                  self.penup()
                  self.hideturtle()
                  self.color("white")
                  self.goto(postion)
                  
                  self.update_score()
                  
          def update_score(self):
                  self.write(f"score:{self.score}",align="center",font=("courier",20,"normal"))
         
          def increase_score(self):
                  self.score +=1
                  self.clear()
                  self.update_score() 
          def game_over(self):
                  self.clear()
                  self.screen.bgcolor("darkred")
                  self.goto(0,0)
                  if self.score>self.high_score:
                          self.high_score=self.score
                  self.write(f"--------- Game Over ---------\n\nFinal Score: {self.score} \n\n High Score : {self.high_score}",align="center",font=("courier",20,"normal"))        
                  
                        
                          