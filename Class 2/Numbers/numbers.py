n = input("Number: ")
num = float(n)
counter = 1
prime = True

while counter < num:

    if num % counter == 0:
        prime = False

        break

    counter = counter + 1

def poc():

    if prime:

        print("This is a prime number!")

    else:

        print("This is a composite number.")

def decimal():

    if num > 0 and num != 0:

        print("This number is a natural number.")

        poc()

    else:

        print("This is a rational number.")

if n.isdecimal() == True:

    if num % 2 == 0:

        print("This number is even.")

        decimal()

    elif num % 2 != 0:

        print("This number is odd.")

        poc()

elif n.isdecimal() == False:

    decimal()