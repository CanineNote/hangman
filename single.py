'''
Created on Mar 2, 2020

@author: Bryson
'''
import sys
sys.stdout.flush()
import random
global players
import importantvars

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

players = 1

if (players == 1):
    def findValue(x, value):
        indices = list()
        for i in range(len(x)):
            if x[i] == value:
                indices.append(i)
        return indices

    m = True;
    def singleplayer():
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
        while m == True:
            while True:
                z = input("Please input your guess: ")
                if z.isalpha():
                    break
                else:
                    print("The guess must be alphanumeric!")
                    continue
            if (z == chosen):
                print("Congratulations, you've won!")
                check = input("Would you like to play again? (Y/N):\n")
                if (check == "y".lower() or check == "y".upper()):
                    singleplayer()
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
                        print(f"Game over!")
                        print(f"The correct word was {chosen}.")
                        check = input("Would you like to play again? (Y/N):\n")
                        if (check == "y".lower() or check == "y".upper()):
                            singleplayer()
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
                        print("I'm sorry, you've failed! Better luck next time!")
                        check = input("Would you like to play again? (Y/N):\n")
                        if (check == "y".lower() or check == "y".upper()):
                            singleplayer()
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
                    print("Congratulations, you've won!")
                    check = input("Would you like to play again? (Y/N):\n")
                    if (check == "y".lower() or check == "y".upper()):
                        for i in range(100):
                            print("\n")
                        singleplayer()
                        break
                    else:
                        importantvars.count = 10
                        break
