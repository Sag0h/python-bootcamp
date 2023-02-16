from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILE_PATH = r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day20-21-24-snake-game\highscore.txt"
    

class ScoreBoard(Turtle):
    
    def __init__(self):        
        super().__init__()
        self.score = 0
        with open(FILE_PATH, "r") as f:
            try:
                self.highscore = int(f.read())
            except:
                print("warning! highscore file is corrupted. highscore was reset to 0.")
                self.highscore = 0

        self.pu()
        self.ht()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(FILE_PATH, mode="w") as f:
                f.write(str(self.score))
        self.score = 0
        self.update_scoreboard()