from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, text, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.pendown()
        self.color("white")
        self.pencolor("white")
        self.text = text
        self.hideturtle()
        self.write(self.text,False,"left",font=("Arial", 12, "normal"))
        self.score = 0

    def  increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.text+f": {self.score}",False,"left",font=("Arial", 12, "normal"))


