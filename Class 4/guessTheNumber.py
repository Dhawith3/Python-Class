import random

num = random.randint(1, 9)
guess = False
counter = 1

while not guess:

        usernum = int(input("Guess the number from 1 - 9!"))
        counter = counter + 1

        if usernum == num:
            guess = True
        elif usernum < num:
            print("Too low!")
        else:
            print("Too high!")

        if counter > 3 and not guess:
            print("Too many guesses!")

            break

if guess:
    print("You guessed it right!")
else:
    print(f"You lost! The number was {num}")