from turtle import *

sides = int(input("How many sides does your polygon have? "))
length = int(input("How long do you want your polygon to be? "))
size = int(input("How thick do you want the pen to be? "))
border = str(input("What border color do you want you polygon to have? "))
fill = str(input("What fill color do you want you polygon to have? "))

i = 1

penup()

pensize(size)
color(border, fill)

goto(-200, -200)

pendown()

begin_fill()

while i <= sides:

    forward(length)
    left(360/sides)

    i = i + 1

end_fill()

done()
