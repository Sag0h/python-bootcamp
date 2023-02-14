from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            t = Turtle(shape="square")
            t.shapesize(stretch_len=2, stretch_wid=1)
            t.color(random.choice(COLORS))
            t.pu()
            t.goto(300, random.randint(-250, 250))
            t.seth(180)
            self.cars.append(t)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -300:
                self.cars.remove(car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
