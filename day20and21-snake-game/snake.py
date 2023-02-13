from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
DOWN= 270
UP= 90
LEFT= 180
RIGHT= 0
class Snake():

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]


    def create_snake(self):
        pos = 0
        for i in range(3):
            self.parts.append(Turtle("square"))
            self.parts[i].fillcolor("white")
            self.parts[i].pu()
            self.parts[i].goto(STARTING_POSITIONS[i])

    def grow(self):
        self.parts.append(Turtle("square"))
        self.parts[len(self.parts)-1].fillcolor("white")
        self.parts[len(self.parts)-1].pu()
        self.parts[len(self.parts)-1].goto(self.parts[len(self.parts)-1].pos())

    def move(self):
        for i in range(len(self.parts)-1, 0, -1):
            self.parts[i].goto(self.parts[i-1].pos())
        self.head.forward(20)
    
    def up(self):
        h = self.head.heading()
        if( h != DOWN ):
            self.head.seth(UP)

    def down(self):
        h = self.head.heading()
        if( h != UP ):            
            self.head.seth(DOWN)

    def left(self):
        h = self.head.heading()
        if( h != RIGHT ):            
            self.head.seth(LEFT)

    def right(self):
        h = self.head.heading()
        if( h != LEFT ):
            self.head.seth(RIGHT)
    