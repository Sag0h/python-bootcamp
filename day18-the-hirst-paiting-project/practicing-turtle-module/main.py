from turtle import Turtle, Screen
import random

t = Turtle()

screen = Screen()
screen.colormode(255)

def random_color():
    ## returns a random rgb in a tuple.
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# DIBUJA FIGURAS GEOMETRICAS:
# for i in range(3,11):
#     random_rgb = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     t.pencolor(random_rgb) 
#     for j in range(i):
#         t.forward(100)
#         t.right(360/(i))
#RANDOM WALK:

# cardinal_points = [0, 90, 180, 270]
t.speed('fastest')
# t.pensize(10)
# while True:
#     random_rgb = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     t.pencolor(random_rgb) 
#     t.right(random.choice(cardinal_points))
#     t.forward(25)

#SPIROGRAPH:
def draw_spirograph(size):
    for i in range(int(360/size)):
        t.pencolor(random_color()) 
        t.seth(t.heading() + size)
        t.circle(100)

draw_spirograph(5)

screen.exitonclick()