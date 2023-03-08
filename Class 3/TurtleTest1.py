from turtle import *

color("purple", "pink")
pensize(5)
i = 0
sides = 3

begin_fill()
while i < sides:
    forward(100)
    left(360/sides)
    i = i + 1

end_fill()

done()