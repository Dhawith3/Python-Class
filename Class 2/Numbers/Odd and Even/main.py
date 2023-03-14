ooe = str(input("Do you want to list the odd numbers or even numbers? ( o or e ) "))

addend = 0
counter = 1

if ooe == 'o':

    s = int(input("What odd number do you want to start at? "))
    l = int(input("How long do you want it to go? "))

    while counter >= l:

        print(s)

        addend = addend + s
        s = s + 2
        counter = counter + 1

    yn = str(input("Do you want to find the addend of all of these odd numbers? ( y or no ) "))

    if yn == 'y':

        print(f"{addend} is the addend of all of these odd numbers.")

elif ooe == 'e':

    s = int(input("What even number do you want to start at? "))
    l = int(input("How long do you want it to go? "))

    while counter >= l:
        print(s)

        addend = addend + s
        s = s + 2
        counter = counter + 1

    yn = str(input("Do you want to find the addend of all of these even numbers? ( y or no ) "))

    if yn == 'y':
        print(f"{addend} is the addend of all of these even numbers.")
