def temperature():

    fts = str(input("What temperature scale are you from? "))
    tts = str(input("What temperature scale do you want to turn it into? "))

    if fts == 'fahrenheit' and tts == 'celsius':

        f = int(input("What is the fahrenheit? "))

        c = (f - 32) * 5 / 9

        print(f"{f} degrees in fahrenheit is the same as {c} degrees in celsius.")

    elif fts == 'fahrenheit' and tts == 'kelvin':

        f = int(input("What is the fahrenheit? "))

        k = (f + 459.67) * 5 / 9

        print(f"{f} degrees in fahrenheit is the same as {k} degrees in kelvin.")

    elif fts == 'celsius' and tts == 'fahrenheit':

        c = int(input("What is the celsius? "))

        f = c * 9 / 5 + 32

        print(f"{c} degrees in celsius is the same as {f} degrees in fahrenheit.")

    elif fts == 'celsius' and tts == 'kelvin':

        c = int(input("What is the celsius? "))

        k = c + 273.15

        print(f"{c} degrees in celsius is the same as {k} degrees in kelvin.")

    elif fts == 'kelvin' and tts == 'celsius':

        k = int(input("What is the kelvin? "))

        c = k - 273.15

        print(f"{k} degrees in kelvin is the same as {c} degrees in celsius.")

    elif fts == 'kelvin' and tts == 'fahrenheit':

        k = int(input("What is the kelvin? "))

        f = 1.8 * (k - 273) + 32

        print(f"{k} degrees in kelvin is the same as {f} degrees in fahrenheit.")

    else:

        print("Please type fahrenheit, celsius, or kelvin. All lowercase.")

temperature()

yn = str(input("Do you want to do it again? "))

if yn == 'yes':
    temperature()