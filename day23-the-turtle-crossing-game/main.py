import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.title("My turtle crossing game!")
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)
game_is_on = True


while game_is_on:
    car_manager.create_car()

    for car in car_manager.cars:
        if (player.distance(car) <= 20) or (player.distance(x=car.xcor()+12, y=car.ycor()) <= 20) or (player.distance(x= car.xcor()-12, y=car.ycor()) <= 20):
            game_is_on = False
            scoreboard.game_over()
            break
    
    if player.ycor() > 260:
        player.reset_player()
        car_manager.increase_speed()
        scoreboard.level_up()

    screen.update()
    time.sleep(0.1)
    car_manager.move()    