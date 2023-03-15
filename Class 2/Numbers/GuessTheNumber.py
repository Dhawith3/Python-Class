import random
from itertools import repeat

level = str(input("Choose a level ( easy, medium, hard ): "))

def game(l):

    counter = 1

    cn = random.randrange(1, l)

    while counter <= 4:

        un = int(input(f"Guess the number ( 1 - {l} ): "))

        if counter == 3:

            print(f"You ran out of lives, the number was {cn}. Do you want to try again ( y or n ) ?")

            yn = str(input())

            if yn == "y":

                game(l)

            else:

                break

        elif un < cn:

            print("Guess higher")

        elif un == cn:

            print("You're right!")

            yn = input("Do you want to play again!? ")

            if yn == "y":

                game(l)

            else:

                break

        elif un > cn:

            print("Guess lower")

        else:

            print("Please guess in between the range.")

        counter = counter + 1

if level == "easy":

    game(10)

elif level == "medium":

    game(50)

elif level == "hard":

    game(100)