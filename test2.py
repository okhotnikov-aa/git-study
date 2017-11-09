# coding : utf-8

import turtle
import random

turtle.speed(0)
while 0 < 1:
    turtle.penup()
    turtle.goto(random.randrange(-200, 200),random.randrange(-200, 200))
    turtle.pendown()
    turtle.fillcolor(random.random(),random.random(),random.random())
    turtle.begin_fill()
    turtle.circle(random.randrange(200))
    turtle.end_fill()