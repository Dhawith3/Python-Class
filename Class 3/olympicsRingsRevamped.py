from turtle import *
d = 50
f = 2.5 * d
penup()
pensize(10)
goto(-200, 100)
pendown()
color("blue")
circle(d)
penup()
goto( -200 + f, 100)
pendown()
color("black")
circle(d)
penup()
goto( (-200 + f) + f, 100)
pendown()
color("red")
circle(d)
penup()
goto( -142, 50)
pendown()
color("yellow")
circle(d)
penup()
goto( -142 + f, 50)
pendown()
color("green")
circle(d)