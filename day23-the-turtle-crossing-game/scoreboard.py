from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        self.lvl = 1
        super().__init__(visible= False)
        self.pu()
        self.goto(-290, 255)
        self.pencolor("black")
        self.write_lvl()

    def write_lvl(self):
        self.write(f"Level: {self.lvl}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

    def level_up(self):
        self.lvl += 1
        self.clear()
        self.write_lvl()