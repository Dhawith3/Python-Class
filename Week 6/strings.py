name = input("Enter your name: ")
counter = 0

while counter < len(name):

    print(name[counter])

    counter = counter + 1

strList = ["Hello", name]

toPrint = ' '.join(strList)

print(toPrint)