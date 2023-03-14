import random

r = "rock"
p = "paper"
s = "scissors"

def game():

    def yn():

        yn = str(input("Do you want to play again? ( y or n ) "))

        if yn == "y":

            game()

        elif yn == "n":

            print("Come back soon!")

        else:

            print("Sorry, there must've been a typo.")

            yn()

    user = str(input("Do you pick rock, paper, or scissors? "))

    computer = random.choice([r, p, s])

    if ( user == r and computer == p ) or ( user == p and computer == s ) or ( user == s and computer == r ):

        print(f"Computer chose {computer} and you lost, :(")

        yn()

    elif ( user == p and computer == r ) or ( user == s and computer == p ) or ( user == r and computer == s ):

        print(f"Computer chose {computer} and you won, :D")

        yn()

    elif user == computer:

        print(f"Computer chose {computer} and you tied, :l")

        yn()

game()
