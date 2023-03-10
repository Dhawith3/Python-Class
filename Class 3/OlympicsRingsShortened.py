from turtle import *

counter = 1
xc = 2
yc = 3
cc = 1
xo = -250
xt = -140
yo = 100
yt = -25
add = 220

colors = ["blue", "black", "red", "yellow", "green"]
posarray = [xo, yo, xo + add, yo, xo + add * 2, yo, xt, yt, xt + add, yt]

x = posarray[0]
y = posarray[1]
c = colors[0]

pensize(8)

def ring(x, y, c):

    penup()

    goto(x, y)
    color(f"{c}")

    pendown()

    circle(100)

while counter <= 5:

    ring(x, y, c)

    x = posarray[xc]
    y = posarray[yc]
    c = colors[cc]

    xc = xc + 2
    yc = yc + 2
    cc = cc + 1
    counter = counter + 1
