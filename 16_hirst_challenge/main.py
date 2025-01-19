import turtle
import random

color_list = [(177, 59, 36), (239, 224, 2), (2, 99, 76), (215, 63, 123), (130, 36, 20), (245, 231, 46),
              (94, 171, 225), (237, 161, 192), (179, 56, 111), (225, 72, 52), (18, 97, 166), (222, 136, 173),
              (207, 180, 13), (212, 223, 229), (2, 103, 110), (218, 156, 93), (105, 27, 10), (44, 121, 77),
              (17, 25, 35), (208, 221, 216), (137, 30, 44), (236, 220, 173), (70, 162, 87), (240, 194, 215),
              (11, 65, 49), (19, 61, 136), (92, 114, 183), (132, 178, 149), (75, 18, 27), (169, 177, 231)]

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.penup()
i = -200
for _ in range(10):
    timmy.setpos(-300, i)
    for _ in range(10):
        timmy.pencolor(random.choice(color_list))
        timmy.dot(20)
        timmy.forward(65)
    i += 50

screen = turtle.Screen()
screen.exitonclick()
















