from turtle import *
import random

hideturtle()
speed(20)

mode = str(input("One Player or Two Player: "))

if mode == 'One Player':

    words = ["treated", "uncle", "nature", "regular", "direct", "shall", "blind", "grain", "telephone", "highest", "object", "husband", "inside", "damage", "crew", "chosen", "shut", "surface", "dark", "whom", "thumb", "route", "rod", "idea", "alive", "win", "bad", "repeat", "pony", "recently", "watch", "youth", "whole", "larger", "hidden", "rising", "physical", "front", "go", "growth", "laugh", "advice", "point", "handle", "function", "horse", "personal", "mistake", "too", "lost", "local", "regular", "bare", "shoulder", "social", "care", "amount", "us", "planned", "himself", "newspaper", "shelter", "nor", "brush", "brass", "fully", "clear", "bell", "shade", "maybe", "breath", "eager", "card", "hardly", "represent", "consonant", "spin", "regular", "run", "truth", "outline", "dark", "fierce", "school", "grain", "heading", "bicycle", "nor", "courage", "chair", "form", "victory", "weather", "sink", "film", "appearance", "labor", "society", "wash", "certainly", "piano", "fireplace", "picture", "pitch", "wheel", "cutting", "back", "basis", "border", "discover", "part", "group", "made", "lose", "gravity", "basis", "among", "desk", "graph", "war", "potatoes", "replace", "announced", "guide", "manner", "today", "sand", "like", "ready", "plates", "mud", "threw", "tune", "clean", "wolf", "dead", "try", "present", "increase", "ship", "swept", "travel", "feel", "count", "purple", "gray", "driver", "grabbed", "process", "page", "it", "land", "interest", "supper", "twice", "garage", "box", "purple", "throw", "show", "for", "classroom", "desk", "safe", "whose", "while", "plant", "planning", "light", "oxygen", "anybody", "your", "nearly", "earn", "shout", "deal", "stick", "city", "golden", "anywhere", "dropped", "said", "pocket", "wise", "disappear", "plane", "clock", "bring", "bill", "industry", "silence", "rush", "tank", "arrange", "club", "low", "seldom", "game", "able", "may", "he", "grandfather", "airplane", "just", "selection", "pie", "cave", "flight", "strip", "maybe", "some", "without", "floating", "kids", "electricity", "anyway", "positive", "country", "smell", "straight", "black", "uncle", "finger", "applied", "student", "getting", "on", "swim", "harbor", "bar", "captured", "bite", "customs", "because", "tiny", "ability", "available", "team", "flew", "palace", "harbor", "language", "fifteen", "bread", "hearing", "century", "step", "pick", "half", "necessary", "hundred", "beside", "length", "connected", "ranch", "measure", "ten", "essential", "perfectly", "swam", "underline", "mill", "wonder", "drove", "birth", "himself", "valley", "factory", "easily", "tree", "scientific", "two", "pour", "unusual", "dozen", "ability", "native", "how", "pot", "town", "carbon", "nest", "climb", "rope", "worse", "won", "soil", "why", "notice", "table", "decide", "excellent", "setting", "neighbor", "represent", "refer", "cut", "fell", "health", "riding", "live", "constantly", "choice", "harder", "frog", "gun", "leader", "lamp", "rubber", "card", "them", "disease", "term", "general", "similar", "push", "film", "degree", "birth", "gray", "guard", "beginning", "missing", "move", "health", "mill", "feel", "themselves", "affect", "popular", "best", "given", "must", "furniture", "condition", "seven", "way", "had", "happily", "saw", "tie", "came", "object", "drink", "salt", "edge", "eleven", "phrase", "nest", "cold", "indicate", "air", "joy", "surrounded", "pot", "fighting", "explanation", "become", "everybody", "lack", "sat", "all", "forest", "pair", "close", "glad", "needle", "respect", "night", "failed", "football", "rubber", "command", "part", "all", "worth", "decide", "myself", "sort", "missing", "doctor", "to", "diameter", "smaller", "health", "joined", "trick", "seems", "gray", "pressure", "instance", "generally", "supply", "birthday", "behavior", "care", "snow", "read", "led", "pass", "elephant", "chair", "primitive", "ocean", "musical", "friend", "atom", "her", "buffalo", "involved", "occasionally", "happen", "number", "raw", "ill", "them", "species", "simple", "package", "living", "favorite", "or", "solution", "upon", "pain", "vast", "meat", "coach", "tight", "fruit", "anywhere", "plenty", "corner", "already", "also", "garden", "fast", "possibly", "managed", "road", "soap", "excellent", "spring", "ago", "useful", "mother", "recently", "yet", "center", "gasoline", "gun", "broad", "meal", "earn", "whistle", "honor", "easy", "hundred", "applied", "whole", "he", "dust", "taste", "action", "moving", "something", "massage", "create", "steam", "told", "special", "hour", "military", "finally", "sheet", "lovely", "became", "mean", "writer", "him", "gave", "snow", "syllable", "part", "explain", "rope", "bottle", "cream", "compass", "noise", "sort", "lovely", "load", "told", "hot", "drove", "section", "ten", "personal", "colony", "position", "somehow", "place", "sun", "firm", "understanding", "make", "fewer", "father", "you", "first", "mother", "fear", "spoken", "tightly", "threw", "teacher", "smell", "total", "nearest", "material", "best", "tube", "essential", "clay", "although", "occasionally", "long", "introduced", "believed", "selection", "girl", "tax", "wing", "control", "strong", "stop", "company", "warn", "tomorrow", "accurate", "purple", "soon", "provide", "forest", "fence", "lead", "smooth", "gentle", "wife", "indeed", "various", "prove", "hospital", "tank", "food", "spring", "along", "rod", "my", "habit", "torn", "excitement", "character", "cent", "red", "tell", "wire", "take", "contain", "blind", "route", "border", "tax", "could", "curve", "sweet", "join", "safety", "badly", "aware", "worried", "stuck", "smallest", "cause", "being", "laugh", "copper", "slipped", "be", "themselves", "trade", "chain", "know", "electric", "knowledge", "learn", "thought", "deal", "grandmother", "medicine", "scientist", "harbor", "join", "cloud", "both", "at", "fur", "view", "by", "telephone", "principle", "disappear", "rule", "full", "industry", "divide", "become", "fun", "his", "held", "source", "grew", "hello", "swim", "using", "animal", "plant", "ready", "led", "neighborhood", "pipe", "morning", "practice", "solar", "can", "land", "manner", "addition", "breakfast", "badly", "purple", "swing", "slipped", "company", "spring", "street", "color", "band", "missing", "take", "glad", "raise", "harbor", "tightly", "common", "passage", "massage", "globe", "community", "nothing", "raw", "finger", "happened", "note", "recognize", "piano", "together", "grown", "whose", "repeat", "rise", "against", "consider", "tip", "breathe", "uncle", "since", "we", "already", "twenty", "use", "experience", "tried", "doubt", "wire", "struck", "remain", "together", "climate", "aside", "crowd", "old", "act", "easier", "fort", "master", "honor", "brought", "them", "factory", "different", "rubber", "wolf", "drop", "dig", "after", "younger", "production", "claws", "human", "position", "gulf", "slowly", "troops", "bet", "setting", "swimming", "mirror", "phrase", "doing", "foot", "short", "troops", "melted", "office", "rain", "drawn", "tiny", "distant", "simple", "telephone", "gasoline", "again", "series", "are", "slight", "under", "whale", "question", "figure", "cave", "equal", "time", "smaller", "strong", "enjoy", "saddle", "bit", "wonderful", "tone", "applied", "column", "across", "experience", "hair", "naturally", "positive", "weigh", "work", "molecular", "hollow", "taste", "were", "join", "properly", "along", "affect", "none", "location", "kill", "son", "pack", "movie", "diagram", "giving", "winter", "park", "heading", "recognize", "living", "needs", "teach", "familiar", "farther", "hungry", "birds", "guess", "people", "become", "none", "bean", "motion", "anyway", "having", "bet", "clay", "task", "hope", "between", "cross", "gun", "mind", "police", "mental", "hope", "molecular", "earn", "be", "fix", "shot", "locate", "by", "high", "unit", "nation", "planned", "some", "deeply", "pony", "replied", "shelf", "passage", "today", "storm", "hall", "mark", "managed", "is", "plant", "weather", "cold", "eight", "rush", "opinion", "base", "prevent", "dust", "social", "bound", "pocket", "donkey", "plastic", "stream", "fifty", "root", "broke", "just", "return", "win", "percent", "average", "every", "may", "lack", "chose", "coat", "warm", "movement", "fly", "wonderful", "hidden", "flow", "occasionally", "vote", "frame", "repeat"]
    word = str(random.choice(words))
    posarray = [-320, -245, -170, -95, -20, 55, 130, 205, 280]
    missed = []
    letters = 0
    m = 0

    for i in range(len(word), 9):
        posarray.pop(0)

    # Lines
    penup()
    goto(170, -175)
    pensize(5)
    pendown()
    forward(150)
    left(90)
    forward(400)
    left(90)
    forward(300)
    left(90)
    forward(100)
    penup()
    goto(320, -300)
    right(90)
    pendown()
    forward(50)

    for i in range(1, len(word)):
        penup()
        forward(25)
        pendown()
        forward(50)

    penup()

    def guess():

        global words
        global word
        global posarray
        global m
        global missed
        global letters

        print(f"Missed Letters: {missed}")
        guess = str(input("What's your guess? "))

        if guess.lower() in word:

            letters = letters + 1

            for l in range(len(word)):

                if guess.lower() == word[l] and guess.lower() == word[0]:

                    goto(posarray[l], -300)
                    write(guess.upper(), font=('Times New Roman', 50, 'normal'))

                    penup()

                elif guess.lower() == word[l]:

                    goto(posarray[l], -300)
                    write(guess.lower(), font=('Times New Roman', 50, 'normal'))

                    penup()

            if letters == len(word):

                print("YOU WIN!")

                done()

        else:

            missed.append(guess.lower())

            if m == 0:

                # head
                goto(20, 125)
                pendown()
                circle(40)

                penup()

                m = 1

            elif m == 1:

                # body
                penup()
                goto(20, 45)
                left(90)
                pendown()
                forward(125)

                penup()

                m = 2

            elif m == 2:

                # left leg
                goto(20, -80)
                pendown()
                right(30)
                forward(115)

                penup()

                m = 3

            elif m == 3:

                # right leg
                goto(20, -80)
                pendown()
                left(60)
                forward(115)

                penup()

                m = 4

            elif m == 4:

                # left hand
                goto(20, -20)
                pendown()
                left(195)
                forward(115)

                penup()

                m = 5

            elif m == 5:

                # right hand
                goto(20, -20)
                pendown()
                right(90)
                forward(115)

                print(f"YOU LOSE! The word was {word}.")

                penup()

                done()

    while m != 5 or letters != len(word):

        guess()

elif mode == 'Two Player':

    word = str(input("What's your word? ( 9 letters is the maximum ) "))
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    posarray = [-320, -245, -170, -95, -20, 55, 130, 205, 280]
    missed = []
    letters = 0
    m = 0

    for i in range(len(word), 9):
        posarray.pop(0)

    # Lines
    penup()
    goto(170, -175)
    pensize(5)
    pendown()
    forward(150)
    left(90)
    forward(400)
    left(90)
    forward(300)
    left(90)
    forward(100)
    penup()
    goto(320, -300)
    right(90)
    pendown()
    forward(50)

    for i in range(1, len(word)):
        penup()
        forward(25)
        pendown()
        forward(50)

    penup()


    def guess():

        global words
        global word
        global posarray
        global m
        global missed
        global letters

        print(f"Missed Letters: {missed}")
        guess = str(input("What's your guess? "))

        if guess.lower() in word:

            letters = letters + 1

            for l in range(len(word)):

                if guess.lower() == word[l] and guess.lower() == word[0]:

                    goto(posarray[l], -300)
                    write(guess.upper(), font=('Times New Roman', 50, 'normal'))

                    penup()

                elif guess.lower() == word[l]:

                    goto(posarray[l], -300)
                    write(guess.lower(), font=('Times New Roman', 50, 'normal'))

                    penup()

            if letters == len(word):
                print("YOU WIN!")

                done()

        else:

            missed.append(guess.lower())

            if m == 0:

                # head
                goto(20, 125)
                pendown()
                circle(40)

                penup()

                m = 1

            elif m == 1:

                # body
                penup()
                goto(20, 45)
                left(90)
                pendown()
                forward(125)

                penup()

                m = 2

            elif m == 2:

                # left leg
                goto(20, -80)
                pendown()
                right(30)
                forward(115)

                penup()

                m = 3

            elif m == 3:

                # right leg
                goto(20, -80)
                pendown()
                left(60)
                forward(115)

                penup()

                m = 4

            elif m == 4:

                # left hand
                goto(20, -20)
                pendown()
                left(195)
                forward(115)

                penup()

                m = 5

            elif m == 5:

                # right hand
                goto(20, -20)
                pendown()
                right(90)
                forward(115)

                print(f"YOU LOSE! The word was {word}.")

                penup()

                done()


    while m != 5 or letters != len(word):
        guess()

done()