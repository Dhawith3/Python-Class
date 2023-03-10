from turtle import *

s = 100
xo = -250
xt = -140
yo = 100
yt = -25
add = 220
pensize(8)

penup()

goto(xo, yo)
color("blue")

pendown()

circle(s)

penup()

goto(xo + add, yo)
color("black")

pendown()

circle(s)

penup()

goto(xo + add * 2, yo)
color("red")

pendown()

circle(s)

penup()

goto(xt, yt)
color("yellow")

pendown()

circle(s)

penup()

goto(xt + add, yt)
color("green")

pendown()

circle(s)

done()
