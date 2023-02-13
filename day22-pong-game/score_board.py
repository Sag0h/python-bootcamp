from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):        
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.pu()
        self.ht()
        self.show_score()


    def show_score(self):
        self.goto(-120, 200)
        self.write(self.lscore, align=ALIGNMENT, font=FONT)
        self.goto(120, 200)
        self.write(self.rscore, align=ALIGNMENT, font=FONT)


    def increase_lscore(self):
        self.lscore += 1
        self.clear()
        self.show_score()

    def increase_rscore(self):
        self.rscore += 1
        self.clear()
        self.show_score()