'''
Created on Mar 3, 2020

@author: Bryson
'''

import sys
sys.stdout.flush()
import random
# Used to grab a random word from the list wordbank
import importantvars
# Grabs the variables stored in importantvars.py



def findValue(x, value):
    indices = list()
    for i in range(len(x)):
        if x[i] == value:
            indices.append(i)
    return indices
# My custom .find() because .find() only finds the first value in a string.

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
# The hangman, more info later.



def multi2():
    wordletters = []
    # A list which gets appended to with the individual characters in the chosen word.
    incorrect = []
    # A list which gets appended to with any value (Alphanumeric specifically) that aren't found in wordletters list

    chosen = random.choice(importantvars.wordbank)
    # Picks a random word from the list, wordbank in importantvars.

    str1 = ""
    # Needed to add to str1
    for x in chosen:
        for y in x:
                str1 = str1 + "_ "
                # For each character, add a "_ "
                wordletters.append(y)
                # Add each character to the list wordletters
    blanks = str1.split(" ")
    # Turn str1 to a list, 'blanks'
    blanks.remove("")
    # Remove the extra "" from the end of the list, as added by the initial variable
    print("\n\n")
    # Seperate to clean
    print(stg0)
    # Print the current skeleton
    print(" ".join(blanks))
    # Print blanks as a string, the length of the word.
    currentstg = stg0
    # Set the currentstg value to stg0, this changes later.
    activeplayer = "Player 1"
    # Set the currently active player, used in the input question.
    checkP1Active = True
    checkP2Active = False
    # Identifiers to see which players are active
    while True:
        # While True do:
        if (checkP1Active == True):
            # If Player 1 is active, then
            while True:
                activeplayer = "Player 1"
                # Make sure it's active, because it changes in the next if statement
                z = input(f"{activeplayer}, please input your guess: ")
                # Asks for the current players' guess
                checkP1Active = False
                # Makes them inactive, and makes the next user in the list active instead.
                checkP2Active = True
                if z.isalpha():
                    break
                    # Checks to see if whatever they entered is alphanumeric, if True then break out of the current loop.
                else:
                    print("The guess must be alphanumeric!")
                    # Checks to see if it isn't, if True then repeat until it is.
                    continue
        elif (checkP2Active == True):
            # Does practically the same thing as above.
            while True:
                activeplayer = "Player 2"
                z = input(f"{activeplayer}, please input your guess: ")
                checkP2Active = False
                checkP1Active = True
                if z.isalpha():
                    break
                else:
                    print("The guess must be alphanumeric!")
                    continue
        if (z == chosen):
            # If the player guesses the word exact the first try, then :
            print(f"Congratulations {activeplayer}, you've won!")
            check = input("Would you like to play again? (Y/N):\n")
            if (check == "y".lower() or check == "y".upper()):
                importantvars.wordbank[0] = input("What word would you like to use for the new game?\n")
                for i in range(100):
                    print("\n")
                multi2()
                # Re-runs the function
                break
            else:
                importantvars.count = 10
                # Changes count, canceling out the loop in Hangman.py
                break
        else:
        # If it wasn't exact, which it probably wasn't, then:
          while True:
        # While True do:
            if (checkP1Active == True):
            # If Player 1 is active, then
              while True:
                activeplayer = "Player 1"
                # Make sure it's active, because it changes in the next if statement
                z = input(f"{activeplayer}, please input your guess: ")
                # Asks for the current players' guess
                checkP1Active = False
                # Makes them inactive, and makes the next user in the list active instead.
                checkP2Active = True
                if z.isalpha():
                    break
                    # Checks to see if whatever they entered is alphanumeric, if True then break out of the current loop.
                else:
                    print("The guess must be alphanumeric!")
                    # Checks to see if it isn't, if True then repeat until it is.
                    continue
                    check = input("Would you like to play again? (Y/N):\n")
                    if (check == "y".lower() or check == "y".upper()):
                            importantvars.wordbank[0] = input("What word would you like to use for the new game?\n")
                            # Updates the original word they were using with whatever they input
                            for i in range(100):
                                print("\n")
                            # Clears the screen
                            multi2()
                            break
                    else:
                            importantvars.count = 10
                            break
                            # Adds to the variable count, stopping function from ever being ran and ending the entire file.
        z = z.lower()
        # Changes it to lowercase, so it properly checks the rest of the letters.
        # The code probably breaks if you do words like = 'ImSupErTiReD' because it has capitalization in a place it shouldn't. I think this is the only error.
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
                        multi2()
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
                    for i in range(100):
                            print("\n")
                    multi2()
                    break
                else:
                    importantvars.count = 10
                    break
