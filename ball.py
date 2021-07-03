from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed("slowest")
        self.ycor_sign = 1
        self.xcor_sign = 1
    def check_collision_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.ycor_sign = -1 * self.ycor_sign

    def check_collision_paddle(self,paddle):
        if paddle.xcor() > 0:
            if 10 < -self.xcor()+paddle.xcor() < 30 and abs(self.ycor()-paddle.ycor()) < 50:
                self.xcor_sign = self.xcor_sign * -1
        if paddle.xcor() < 0:
            if 10 < self.xcor()-paddle.xcor() < 30 and abs(self.ycor()-paddle.ycor()) < 50:
                self.xcor_sign = self.xcor_sign * -1


    def in_bounds(self):
        return  -400 < self.xcor() < 400





    def move(self,l_paddle,r_paddle):

        self.check_collision_wall()
        self.check_collision_paddle(l_paddle)
        self.check_collision_paddle(r_paddle)



        new_x = self.xcor()+ self.xcor_sign * 2
        new_y = self.ycor() + self.ycor_sign * 2

        self.goto(new_x,new_y)