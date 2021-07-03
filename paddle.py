from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        self.penup()
        self.color("white")
        self.speed("fastest")

    def up(self):
        if self.ycor()<240:
            self.goto(self.xcor(),self.ycor()+40)
    def down(self):
        if -240 < self.ycor():
            self.goto(self.xcor(),self.ycor()-40)
