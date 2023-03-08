import random

user = input("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors! ")
computer = random.choice(['r', 'p', 's'])
r = "rock"
p = "paper"
s = "scissors"
l = ""

if user == 'r' and computer == 's':
    print(f"Computer selected scissors and you won!")
elif user == 'p' and computer == 'r':
    print(f"Computer selected rock and you won!")
elif user == 's' and computer == 'p':
    print(f"Computer selected paper and you won!")
elif user == 'p' and computer == 'p':
    print(f"Computer selected paper and it's a tie!")
elif user == 's' and computer == 's':
    print(f"Computer selected scissors and it's a tie!")
elif user == 'r' and computer == 'r':
    print(f"Computer selected rock and it's a tie!")
else:
    if computer == 'r':
        l = r
    elif computer == 'p':
        l = p
    else:
        l = s
    print(f"Computer selected {l} and you lost!")