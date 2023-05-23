import customtkinter as ctk
import random

currentText = ""


def updateText():

    global currentText

    if len(currentText) == 0:
        currentText = ""

    if len(currentText) > 12:
        currentText = currentText[:12]

    Label.configure(text=currentText)

def addText(str):

    global currentText

    currentText = str
    infoLabel.configure(text="")
    updateText()

def clear():

    global currentText

    currentText = ""
    infoLabel.configure(text="")
    updateText()

def check():

    global currentText

    r = "Rock"
    p = "Paper"
    s = "Scissors"

    computer = random.choice([r, p, s])
    user = currentText

    if ( user == r and computer == p ) or ( user == p and computer == s ) or ( user == s and computer == r ):

        infoLabel.configure(text=f"Computer chose {computer} and you lost.")

    elif ( user == p and computer == r ) or ( user == s and computer == p ) or ( user == r and computer == s ):

        infoLabel.configure(text=f"Computer chose {computer} and you won!")

    elif user == computer:

        infoLabel.configure(text=f"Computer chose {computer} and you tied.")


app = ctk.CTk()
app.geometry("390x417.5")
app.title("Rock Paper Scissors")

# App's Background Color
app.configure(bg_color="white", fg_color="white")

# Frame
Frame = ctk.CTkFrame(app, width=330, height=10, bg_color="white", fg_color="white")
Frame.grid(row=0, column=0, padx=10, pady=10)

VisualFrame = ctk.CTkFrame(app, width=330, height=10, bg_color="white", fg_color="white")
VisualFrame.grid(row=1, column=0, padx=10, pady=10)

# Frame Labels

Label = ctk.CTkLabel(Frame, text="", width=330, height=50, font=ctk.CTkFont(size=60), anchor="e")
Label.grid(row=0, column=0, padx=10)

infoLabel = ctk.CTkLabel(Frame, text="", width=330, height=10, font=ctk.CTkFont(size=20), anchor="e")
infoLabel.grid(row=1, column=0, padx=10)

check = ctk.CTkButton(VisualFrame, text="Check", fg_color="#d9d9d9", hover_color="#CCCCCC", text_color="black", width=167.5,
                     height=20, font=ctk.CTkFont(size=20), command=check)
check.grid(row=0, column=0, padx=10, pady=10)

clear = ctk.CTkButton(VisualFrame, text="Clear", fg_color="#d9d9d9", hover_color="#CCCCCC", text_color="black", width=167.5,
                      height=20, font=ctk.CTkFont(size=20), command=clear)
clear.grid(row=0, column=1, padx=10)

# Button Frame
btnFrame = ctk.CTkFrame(app, width=350, height=420, bg_color="white", fg_color="white")
btnFrame.grid(row=2, column=0, padx=10)

# Choices

BtnR = ctk.CTkButton(btnFrame, text="Rock", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=360,
                     height=64, font=ctk.CTkFont(size=20), command=lambda : addText("Rock"))
BtnR.grid(row=1, column=0, padx=5, pady=5)

BtnP = ctk.CTkButton(btnFrame, text="Paper", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=360,
                     height=64, font=ctk.CTkFont(size=20), command=lambda : addText("Paper"))
BtnP.grid(row=2, column=0, padx=5, pady=5)

BtnS = ctk.CTkButton(btnFrame, text="Scissors", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=360,
                     height=64, font=ctk.CTkFont(size=20), command=lambda : addText("Scissors"))
BtnS.grid(row=3, column=0, padx=5, pady=5)

app.mainloop()
