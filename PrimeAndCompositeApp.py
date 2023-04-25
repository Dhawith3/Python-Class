import customtkinter as ctk

def enter_clicked():

    num = int(choiceEntry.get())

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
app.geometry("500x300")
app.title("Prime and Composite")

choiceLabel = ctk.CTkLabel(app, text="Number: ")
choiceLabel.grid(row=0, column=0)

choiceEntry = ctk.CTkEntry(app, placeholder_text="Enter your number")
choiceEntry.grid(row=0, column=1)

enterButton = ctk.CTkButton(app, text="Check", command=enter_clicked)
enterButton.grid(row=0, column=2)

infoLabel = ctk.CTkLabel(app, text="")
infoLabel.grid(row=1, column=0)

app.mainloop()