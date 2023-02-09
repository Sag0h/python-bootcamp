from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("The turtle racing game!")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

def draw_start_point():
    t = Turtle()
    t.speed("fastest")
    t.ht()
    t.pu()
    t.goto(x=-230, y=-200)
    t.pd()
    t.seth(90)
    t.forward(400)

def draw_end_point():
    t = Turtle()
    t.speed("fastest")
    t.ht()
    t.pu()
    t.goto(x=239, y=-200)
    t.pd()
    t.seth(90)
    t.forward(400)

colors = ["red", "orange", "yellow", "green", "deep sky blue" ,"blue", "purple"]
turtles = []
num = -150
draw_start_point()
draw_end_point()
for i in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].pu()
    turtles[i].goto(x=-240, y=num)
    num += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        if turtle.xcor() < 230:
            turtle.forward(rand_distance)
        else:
            winner = turtle
            is_race_on = False
            break

print(f"{turtle.fillcolor()}")
if turtle.fillcolor() == user_bet:
    print("You win.")
else:
    print("You lose.")
screen.exitonclick()