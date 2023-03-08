from turtle import *

def polygon( sides, length ):

    color("purple", "pink")
    pensize(3)

    begin_fill()

    i = 0
    while i < sides:
        forward(length)
        left(360/sides)
        i = i + 1

    end_fill()

s = int(input("How many sides do you want your polygon to be? "))
l = int(input("How long do you want your polygon to be? "))

polygon( s, l )

done()