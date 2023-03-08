from turtle import *

color("purple", "pink")
pensize(2)

begin_fill()
while True:
    forward(200)
    left(130)
    if abs(pos()) < 1:
        break

end_fill()

penup()
goto(-200, -100)
pendown()
i = 0
sides = 3
begin_fill()
while True:
    forward(200)
    left(130)
    if abs(pos()) < 1:
        break

end_fill()

done()