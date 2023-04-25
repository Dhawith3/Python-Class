import customtkinter as ctk
import random

def enter_clicked():

    r = "rock"
    p = "paper"
    s = "scissors"

    computer = random.choice([r, p, s])
    user = choiceEntry.get()

    if ( user == r and computer == p ) or ( user == p and computer == s ) or ( user == s and computer == r ):

        infoLabel.configure(text=f"Computer chose {computer} and you lost, :(")

    elif ( user == p and computer == r ) or ( user == s and computer == p ) or ( user == r and computer == s ):

        infoLabel.configure(text=f"Computer chose {computer} and you won, :D")

    elif user == computer:

        infoLabel.configure(text=f"Computer chose {computer} and you tied, :l")

app = ctk.CTk()
app.geometry("500x300")
app.title("Rock Paper Scissors")

choiceLabel = ctk.CTkLabel(app, text="Rock, Paper, or Scissors: ")
choiceLabel.grid(row=0, column=0)

choiceEntry = ctk.CTkEntry(app, placeholder_text="Enter your choice")
choiceEntry.grid(row=0, column=1)

enterButton = ctk.CTkButton(app, text="Enter", command=enter_clicked)
enterButton.grid(row=0, column=2)

infoLabel = ctk.CTkLabel(app, text="")
infoLabel.grid(row=1, column=0)

app.mainloop()