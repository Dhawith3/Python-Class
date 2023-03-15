num = int(input("Enter any number: "))

counter = 2

prime = True

while counter < num:

    if num % counter == 0:

        prime = False

        break

    counter = counter + 1

if prime:

    print("This is a prime number!")

else:

    print("This is a composite number!")