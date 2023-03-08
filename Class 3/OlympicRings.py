from turtle import *

pensize(10)
f = 2.5 * 50

def rings( x, y):
    penup()
    goto(x, y)
    pendown()
    color("black")
    circle(50)

rings(-200, 100)
rings(-200 + f, 100)
rings((-200 + f) + f, 100)
rings(-142, 50)
rings(-142 + f, 50)