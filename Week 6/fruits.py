counter = 1
fruit = []

def fruits(list):

    global fruit

    fruit.append(list)

while counter <= 3:

    f = input("Fruit: ")
    fruits(f)

    counter = counter + 1

print(", ".join(fruit))