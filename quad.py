'''
Created on Mar 3, 2020

@author: Bryson
'''
import sys
sys.stdout.flush()
import random
global players
import importantvars

def findValue(x, value):
    indices = list()
    for i in range(len(x)):
        if x[i] == value:
            indices.append(i)
    return indices

activeplayer = "Player 1"
global checkP1Active
checkP1Active = True
global checkP2Active
checkP2Active = False

stg0 = """
      +---+
      |   |
          |
          |
          |
     ======
    """
stg1 = """
      +---+
      |   |
      O   |
          |
          |
     ======
    """
stg2 = """
      +---+
      |   |
      O   |
     /    |
          |
     ======
     """
stg3 = """
      +---+
      |   |
      O   |
     /|   |
          |
     ======
     """
stg4 = """
      +---+
      |   |
      O   |
     /|\  |
          |
     ======
     """
stg5 = """
      +---+
      |   |
      O   |
     /|\  |
     /    |
     ======
    """
stg6 = """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
     ======
    """


def multi4():
    wordletters = []
    incorrect = []

    chosen = random.choice(importantvars.wordbank)

    str1 = ""
    for x in chosen:
        for y in x:
            if (y == " "):
                str1 = str1 + "/ "
            else:
                str1 = str1 + "_ "
                wordletters.append(y)
    blanks = str1.split(" ")
    blanks.remove("")
    print("\n\n")
    print(stg0)
    print(" ".join(blanks))
    m = True
    currentstg = stg0
    activeplayer = "Player 1"
    checkP1Active = True
    checkP2Active = False
    checkP3Active = False
    checkP4Active = False
    while m == True:
        if (checkP1Active == True):
            while True:
                activeplayer = "Player 1"
                z = input(f"{activeplayer}, please input your guess: ")
                checkP1Active = False
                checkP2Active = True
                checkP3Active = False
                checkP4Active = False
                if z.isalpha():
                    break
                else:
                    print("The guess must be alphanumeric!")
                    continue
        elif (checkP2Active == True):
            while True:
                activeplayer = "Player 2"
                z = input(f"{activeplayer}, please input your guess: ")
                checkP1Active = False
                checkP2Active = False
                checkP3Active = True
                checkP4Active = False
                if z.isalpha():
                    break
                else:
                    print("The guess must be alphanumeric!")
                    continue
        elif (checkP3Active == True):
            while True:
                activeplayer = "Player 3"
                z = input(f"{activeplayer}, please input your guess: ")
                checkP1Active = False
                checkP2Active = False
                checkP3Active = False
                checkP4Active = True
                if z.isalpha():
                    break
                else:
                    print("The guess must be alphanumeric!")
                    continue
        elif (checkP4Active == True):
            while True:
                activeplayer = "Player 4"
                z = input(f"{activeplayer}, please input your guess: ")
                checkP1Active = True
                checkP2Active = False
                checkP3Active = False
                checkP4Active = False
                if z.isalpha():
                    break
                else:
                    print("The guess must be alphanumeric!")
                    continue
        if (z == chosen):
            print(f"Congratulations {activeplayer}, you've won!")
            check = input("Would you like to play again? (Y/N):\n")
            if (check == "y".lower() or check == "y".upper()):
                importantvars.wordbank[0] = input("What word would you like to use for the new game?\n")
                for i in range(100):
                                print("\n")
                multi4()
                break
            else:
                importantvars.count = 10
                break
        else:
                if (len(z) > 1):
                    incorrect.append(z)
                    if (currentstg == stg0):
                        currentstg = stg1
                        print(', '.join(incorrect))
                        print(currentstg)
                        print(' '.join(blanks))
                        print("\n Your previous guess was incorrect!")
                        continue
                    if (currentstg == stg1):
                        currentstg = stg2
                        print(', '.join(incorrect))
                        print(currentstg)
                        print(' '.join(blanks))
                        print("\n Your previous guess was incorrect!")
                        continue
                    if (currentstg == stg2):
                        currentstg = stg3
                        print(', '.join(incorrect))
                        print(currentstg)
                        print(' '.join(blanks))
                        print("\n Your previous guess was incorrect!")
                        continue
                    if (currentstg == stg3):
                        currentstg = stg4
                        print(', '.join(incorrect))
                        print(currentstg)
                        print(' '.join(blanks))
                        print("\n Your previous guess was incorrect!")
                        continue
                    if (currentstg == stg4):
                        currentstg = stg5
                        print(', '.join(incorrect))
                        print(currentstg)
                        print(' '.join(blanks))
                        print("\n Your previous guess was incorrect!")
                        continue
                    if (currentstg == stg5):
                        currentstg = stg6
                        print(', '.join(incorrect))
                        print(currentstg)
                        print(f"Wow, way to ruin it for everyone {activeplayer}!")
                        print(f"The correct word was {chosen}.")
                        check = input("Would you like to play again? (Y/N):\n")
                        if (check == "y".lower() or check == "y".upper()):
                            importantvars.wordbank[0] = input("What word would you like to use for the new game?\n")
                            for i in range(100):
                                print("\n")
                            multi4()
                            break
                        else:
                            importantvars.count = 10
                            break
        z = z.lower()
        print("\n")
        y = findValue(chosen, z)
        op = (' '.join(blanks))
        uptown = z.upper()
        if (uptown == chosen[0]):
            blanks[0] = z.upper()
            print(currentstg)
            print(' '.join(blanks))
            continue
        if (op.find(z) != -1):
            print("You've already used that letter.")
            continue
        if ((", ".join(incorrect)).find(z) != -1):
            print("You've already used that letter.")
            continue
        if (z != chosen):
            if (y == 0):
                for i in y:
                    blanks[i] = z
            if (y == [] and chosen.find(z) == -1):
                incorrect.append(z)
            if (y != -1):
                for i in y:
                    blanks[i] = z
                if (len(incorrect) == 6):
                    currentstg = stg6
                    print(currentstg)
                    print(f"Wow way to ruin it for everyone {activeplayer}!")
                    print(f"The correct word was {chosen}.")
                    check = input("Would you like to play again? (Y/N):\n")
                    if (check == "y".lower() or check == "y".upper()):
                        importantvars.wordbank[0] = input("What word would you like to use for the new game?\n")
                        for i in range(100):
                                print("\n")
                        multi4()
                        break
                    else:
                        importantvars.count = 10
                        break
                    break
                if (len(incorrect) == 5):
                    currentstg = stg5
                if (len(incorrect) == 4):
                    currentstg = stg4
                if (len(incorrect) == 3):
                    currentstg = stg3
                if (len(incorrect) == 2):
                    currentstg = stg2
                if (len(incorrect) == 1):
                    currentstg = stg1
                if (len(incorrect) == 0):
                    currentstg = stg0
                print(", ".join(incorrect))
                print(currentstg)
                op = (' '.join(blanks))
                print(op)
            if (blanks == wordletters):
                print(f"Congratulations {activeplayer}, you've won!")
                check = input("Would you like to play again? (Y/N):\n")
                if (check == "y".lower() or check == "y".upper()):
                    importantvars.wordbank[0] = input("What word would you like to use for the new game?\n")
                    for i in range(100):
                            print("\n")
                    multi4()
                    break
                else:
                    importantvars.count = 10
                    break
