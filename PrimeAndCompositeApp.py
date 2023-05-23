import customtkinter as ctk

currentText = "0"


def updateText():

    global currentText

    if len(currentText) == 0:
        currentText = "0"

    if len(currentText) > 12:
        currentText = currentText[:12]

    Label.configure(text=currentText)

def addText(str):

    global currentText

    if float(currentText) == 0 and str != '.' and '.' not in currentText:
        currentText = ""

    if '.' in currentText and str == '.':
        return

    currentText = currentText + str
    updateText()

def clear():

    global currentText

    currentText = "0"
    updateText()

def check():

    global currentText

    num = int(currentText)

    counter = 2

    prime = True

    while counter < num:

        if num % counter == 0:

            prime = False

            break

        counter = counter + 1

    if prime:

        infoLabel.configure(text="This is a prime number!")

    else:

        infoLabel.configure(text="This is a composite number!")


app = ctk.CTk()
app.geometry("360x497.5")
app.title("Prime and Composite")

# App's Background Color
app.configure(bg_color="white", fg_color="white")

# Frame
Frame = ctk.CTkFrame(app, width=310, height=10, bg_color="white", fg_color="white")
Frame.grid(row=0, column=0, padx=10, pady=10)

VisualFrame = ctk.CTkFrame(app, width=310, height=10, bg_color="white", fg_color="white")
VisualFrame.grid(row=1, column=0, padx=10, pady=10)

# Frame Labels

Label = ctk.CTkLabel(Frame, text="0", width=310, height=50, font=ctk.CTkFont(size=60), anchor="e")
Label.grid(row=0, column=0, padx=10)

infoLabel = ctk.CTkLabel(Frame, text="", width=310, height=10, font=ctk.CTkFont(size=20), anchor="e")
infoLabel.grid(row=1, column=0, padx=10)

check = ctk.CTkButton(VisualFrame, text="Check", fg_color="#d9d9d9", hover_color="#CCCCCC", text_color="black", width=150,
                     height=20, font=ctk.CTkFont(size=20), command=check)
check.grid(row=0, column=0, padx=10, pady=10)

clear = ctk.CTkButton(VisualFrame, text="Clear", fg_color="#d9d9d9", hover_color="#CCCCCC", text_color="black", width=150,
                      height=20, font=ctk.CTkFont(size=20), command=clear)
clear.grid(row=0, column=1, padx=10)

# Button Frame
btnFrame = ctk.CTkFrame(app, width=330, height=420, bg_color="white", fg_color="white")
btnFrame.grid(row=2, column=0, padx=10)

# Row 1

Btn7 = ctk.CTkButton(btnFrame, text="7", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("7"))
Btn7.grid(row=1, column=0, padx=5, pady=5)

Btn8 = ctk.CTkButton(btnFrame, text="8", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("8"))
Btn8.grid(row=1, column=1, padx=5, pady=5)

Btn9 = ctk.CTkButton(btnFrame, text="9", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("9"))
Btn9.grid(row=1, column=2, padx=5, pady=5)

# Row 2

Btn4 = ctk.CTkButton(btnFrame, text="4", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("4"))
Btn4.grid(row=2, column=0, padx=5, pady=5)

Btn5 = ctk.CTkButton(btnFrame, text="5", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("5"))
Btn5.grid(row=2, column=1, padx=5, pady=5)

Btn6 = ctk.CTkButton(btnFrame, text="6", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("6"))
Btn6.grid(row=2, column=2, padx=5, pady=5)

# Row 3

Btn1 = ctk.CTkButton(btnFrame, text="1", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("1"))
Btn1.grid(row=3, column=0, padx=5, pady=5)

Btn2 = ctk.CTkButton(btnFrame, text="2", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("2"))
Btn2.grid(row=3, column=1, padx=5, pady=5)

Btn3 = ctk.CTkButton(btnFrame, text="3", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("3"))
Btn3.grid(row=3, column=2, padx=5, pady=5)

# Row 4

Btn0 = ctk.CTkButton(btnFrame, text="0", fg_color="#F2F2F2", hover_color="#e6e6e6", text_color="black", width=100,
                     height=64, font=ctk.CTkFont(size=30), command=lambda : addText("0"))
Btn0.grid(row=4, column=1, padx=5, pady=5)

app.mainloop()
