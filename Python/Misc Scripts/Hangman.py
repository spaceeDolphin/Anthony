import numpy as np
import random as r

sample_space = np.array(["elefant", "melkekartong", "nigeria", "flatskjerm", "tyskland"])

word = r.choice(sample_space)
guessedLetters = np.array([])
fail = 0
run = True

print("Gjett en bokstav som er i ordet")
def out():
    out = "i"
    
    for letter in word:
        letterGuessed = False
        for guesses in guessedLetters:
            if letter == guesses:
                print("tag")
                out = out + guesses
                letterGuessed = True
        if not letterGuessed:
            out = out + " _ "
            complete = False
    if complete:
        print("Stop")
        return False
    else:
        return True
        print(out)


while run:
    run = out()
    guess = input()

    if guess in word:
        print("Riktig,", guess, "er i ordet")
        guessedLetters = np.append(guessedLetters, guess)
    else:
        print("Feil")
        fail += 1
        
print("Ord fullført med", fail, "feil")
