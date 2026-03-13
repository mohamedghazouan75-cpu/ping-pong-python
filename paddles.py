from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.penup()
        self.goto(position)
        self.shapesize(5,1)
    def up(self):
        self.goto(self.xcor(),self.ycor()+40) 
    def down(self):
        self.goto(self.xcor(),self.ycor()-40)
    
       