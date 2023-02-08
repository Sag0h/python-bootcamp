
from turtle import Screen, Turtle
import random

rgb_colors = [(220, 145, 91), (116, 162, 216), (47, 102, 162), (242, 76, 34), (241, 232, 236), 
(144, 62, 88), (181, 58, 36), (244, 206, 74), (47, 132, 63), (229, 78, 100), (222, 121, 150), (120, 199, 150), 
(195, 149, 49), (54, 166, 134), (128, 219, 189), (55, 51, 128), (81, 45, 33), (103, 103, 173), (246, 159, 149), (15, 104, 44), 
(253, 200, 0), (62, 45, 55), (100, 90, 6), (43, 30, 67), (125, 40, 47), (155, 216, 223), (231, 166, 178), (46, 67, 55), (130, 42, 34), 
(172, 186, 223), (74, 150, 164)]

screen = Screen()
t = Turtle()
t.pu()
t.speed('fastest')
t.ht()
t.seth(135)
t.forward(350)
t.seth(0)
screen.colormode(255)


number_of_dots = 10

for i in range(number_of_dots):
    for j in range(number_of_dots-1):
        t.dot(20, random.choice(rgb_colors))
        t.forward(50)
    t.dot(20, random.choice(rgb_colors))
    t.seth(270)
    t.forward(50)
    if i % 2 == 0:
        t.seth(180)
    else:
        t.seth(0)
screen.exitonclick()