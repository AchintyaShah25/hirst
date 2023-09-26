from turtle import Turtle, Screen, colormode
import random

import colorgram as cg
colors = cg.extract("IMG_20141228_140342389_HDR.jpg", 6)
colour_li = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    tup = (r, g, b)
    colour_li.append(tup)

colormode(255)
tot = Turtle()
tot.shape("turtle")
tot.speed("fastest")
tot.penup()
tot.hideturtle()
tot.setheading(225)
tot.forward(400)
tot.setheading(0)
dots = 101
for dot in range(1, dots):
    tot.dot(20, random.choice(colour_li))
    tot.forward(50)
    if dot % 10 == 0:
        tot.left(90)
        tot.forward(50)
        tot.left(90)
        tot.forward(500)
        tot.setheading(0)

screen = Screen()
screen.exitonclick()
