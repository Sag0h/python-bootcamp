from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def orient_clockwise():
    t.seth(t.heading() + 10)

def orient_counter_clockwise():
    t.seth(t.heading() - 10)

def clear():
    t.clear()
    t.pu()
    t.home()
    t.pd()

screen.listen()
screen.onkeyrelease(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=orient_clockwise)
screen.onkey(key="d", fun=orient_counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()