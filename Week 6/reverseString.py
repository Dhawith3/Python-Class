def revString(value):
    rev = ""
    counter = len(value) - 1
    while counter >= 0:
        rev = rev + value[counter]
        counter = counter - 1

    print(rev)
    return rev


def palindrome():
    if rev == name:
        print("This is a palindrome.")
    else:
        print("This isn't a palindrome.")

name = input('Enter Name: ')
revString(name)
palindrome()