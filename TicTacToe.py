from turtle import *

hideturtle()
speed(10)

olist = []
xlist = []

# Lines
penup()
goto(-175, 45)
write("A", font=('Courier', 12, 'normal'))
goto(-150, 50)
pendown()
forward(300)
penup()
goto(-175, -55)
write("B", font=('Courier', 12, 'normal'))
goto(-150, -50)
pendown()
forward(300)
penup()
goto(-175, -150)
write("C", font=('Courier', 12, 'normal'))
goto(-50, -150)
pendown()
left(90)
forward(300)
penup()
goto(-55, 170)
write("1", font=('Courier', 12, 'normal'))
penup()
goto(50, -150)
pendown()
forward(300)
penup()
goto(45, 170)
write("2", font=('Courier', 12, 'normal'))
goto(145, 170)
write("3", font=('Courier', 12, 'normal'))

# Move

def xx(a1, a2, b1, b2):
    goto(a1, a2)
    pensize(5)
    left(45)
    pendown()
    color('red')
    forward(110)
    penup()
    goto(b1, b2)
    right(90)
    pendown()
    forward(110)
    penup()
    left(45)

def oo(xr,yr):

    goto(xr, yr)
    pensize(5)
    pendown()
    color('blue')
    circle(35)
    penup()

def o_check():

    if 'A1' in olist and 'A2' in olist and 'A3' in olist:

        right(90)
        goto(-150, 105)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'B1' in olist and 'B2' in olist and 'B3' in olist:

        right(90)
        goto(-150, 0)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'C1' in olist and 'C2' in olist and 'C3' in olist:

        right(90)
        goto(-150, -105)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'A1' in olist and 'B2' in olist and 'C3' in olist:

        right(135)
        goto(-150, 150)
        color('black')
        pendown()
        forward(420)

        done()

    elif 'A3' in olist and 'B2' in olist and 'C1' in olist:

        left(135)
        goto(150, 150)
        color('black')
        pendown()
        forward(420)

        done()

    elif 'A1' in olist and 'B1' in olist and 'C1' in olist:

        goto(-105, -150)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'A2' in olist and 'B2' in olist and 'C2' in olist:

        goto(0, -150)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'A3' in olist and 'B3' in olist and 'C3' in olist:

        goto(100, -150)
        color('black')
        pendown()
        forward(300)

        done()

def x_check():

    if 'A1' in xlist and 'A2' in xlist and 'A3' in xlist:

        right(90)
        goto(-150, 105)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'B1' in xlist and 'B2' in xlist and 'B3' in xlist:

        right(90)
        goto(-150, 0)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'C1' in xlist and 'C2' in xlist and 'C3' in xlist:

        right(90)
        goto(-150, -105)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'A1' in xlist and 'B2' in xlist and 'C3' in xlist:

        right(135)
        goto(-150, 150)
        color('black')
        pendown()
        forward(420)

        done()

    elif 'A3' in xlist and 'B2' in xlist and 'C1' in xlist:

        left(135)
        goto(150, 150)
        color('black')
        pendown()
        forward(420)

        done()

    elif 'A1' in xlist and 'B1' in xlist and 'C1' in xlist:

        goto(-105, -150)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'A2' in xlist and 'B2' in xlist and 'C2' in xlist:

        goto(0, -150)
        color('black')
        pendown()
        forward(300)

        done()

    elif 'A3' in xlist and 'B3' in xlist and 'C3' in xlist:

        goto(100, -150)
        color('black')
        pendown()
        forward(300)

        done()

def move(t, o1, x1, m):

    global olist
    global xlist

    posarray = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    opos = [-70, 105, 35, 105, 135, 105, -70, 0, 35, 0, 135, 0, -70, -105, 35, -105, 135, -105, 0, 0, 0, 0, 0, 0]
    xpos = [-60, 65, -140, 65, 40, 65, -40, 65, 140, 65, 60, 65, -60, -35, -140, -35, 40, -35, -40, -35, 140, -35, 60, -35, -60, -135, -140, -135, 40, -135, -40, -135, 140, -135, 60, -135, 0, 0, 0, 0, 0]
    turns = ['O', 'X']

    a1 = 0
    a2 = 1
    b1 = 2
    b2 = 3
    x = 0
    y = 1
    a = xpos[a1]
    b = xpos[a2]
    c = xpos[b1]
    d = xpos[b2]
    xo = opos[x]
    yo = opos[y]
    counter = 1
    ch = 0

    if t == 'O':

        print("O, it's your turn!")
        move = input("Where do you want to move? (A2, B1, C3, ...) ")
        o1 = o1 + 1

    elif t == 'X':

        print("X, it's your turn!")
        move = input("Where do you want to move? (A2, B1, C3, ...) ")
        x1 = x1 + 1

    m = m + 1

    while counter <= 9:

        if t == 'O':

            if move == posarray[ch]:

                element = posarray[ch]
                index = posarray.index(element)
                olist = olist[:index] + [element] + olist[index:]

                oo(xo, yo)

                break

        elif t == 'X':

            if move == posarray[ch]:

                element = posarray[ch]
                index = posarray.index(element)
                xlist = xlist[:index] + [element] + xlist[index:]

                xx(a, b, c, d)

                break

        a1 = a1 + 4
        a2 = a2 + 4
        b1 = b1 + 4
        b2 = b2 + 4
        a = xpos[a1]
        b = xpos[a2]
        c = xpos[b1]
        d = xpos[b2]
        x = x + 2
        y = y + 2
        xo = opos[x]
        yo = opos[y]
        ch = ch + 1

        counter = counter + 1

move('O', 0, 0, 0)
move('X', 1, 0, 1)
move('O', 1, 1, 2)
move('X', 2, 1, 3)
move('O', 2, 2, 4)
o_check()
move('X', 3, 2, 5)
o_check()
x_check()
move('O', 3, 3, 6)
o_check()
x_check()
move('X', 4, 3, 7)
o_check()
x_check()
move('O', 4, 4, 8)
o_check()
x_check()

print("It was a tie!")

done()