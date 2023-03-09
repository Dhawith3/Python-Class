aoc = str(input("Do you want to find the area or circumference of your circle? ( a or c ) "))

if aoc == 'a':

    dor = str(input("Do you have the diameter or the radius of your circle? ( d or r ) "))

    if dor == 'd':

        d = float(input("What is the diameter of your circle? "))

        u = str(input("What is the unit of your circle? ( plural ) "))

        a = 1 / 4 * 3.14 * d ** 2

        print(f"The area of your circle is {a} {u} squared.")

    elif dor == 'r':

        r = float(input("What is the radius of your circle? "))

        u = str(input("What is the unit of your circle? ( plural ) "))

        a = 3.14 * r ** 2

        print(f"The area of your circle is {a} {u} squared.")

elif aoc == 'c':

    dor = str(input("Do you have the diameter or the radius of your circle? ( d or r ) "))

    if dor == 'd':

        d = float(input("What is the diameter of your circle? "))

        u = str(input("What is the unit of your circle? ( plural ) "))

        c = 3.14 * d

        print(f"The circumference of your circle is {c} {u}.")

    elif dor == 'r':

        r = float(input("What is the radius of your circle? "))

        u = str(input("What is the unit of your circle? ( plural ) "))

        c = 2 * 3.14 * r

        print(f"The circumference of your circle is {c} {u}.")