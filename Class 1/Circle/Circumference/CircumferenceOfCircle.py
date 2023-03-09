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