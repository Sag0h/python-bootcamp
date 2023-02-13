from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)
        self.pu()
        self.color("white")
        self.shape("square")

    def go_up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor()-20)