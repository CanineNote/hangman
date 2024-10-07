'''
Created on Feb 27, 2020

@author: schuellerbry000
'''

'''
Note:
double.py has the most comments in it, explaining the core of the code and how everything works.

quad.py
single.py
triple.py
double.py
all work very similar to one another so to save time I put the comments only in double.py
'''

import time
# used .sleep()
import single
# import singleplayer
from single import singleplayer
from double import multi2
from triple import multi3
from quad import multi4
import importantvars
# where global/module-wide variables are being stored

print('------------------------------------------------')
print('--===========x WELCOME TO HANGMAN x===========--')
print('------------------------------------------------')
#prints the title
time.sleep(.3)
print('  What is Hangman?\n')
time.sleep(.3)
print(' Hangman is, by definiton a guessing game for two or \nmore players. One player thinks of a word, phrase \nor sentence and the other(s) tries to guess it by\nsuggesting letters within a certain number of guesses.\n')
time.sleep(.3)
print('------------------------------------------------')
print('  Meet the Developer!\n')
time.sleep(.3)
print(" Bryson Schueller is the CROWNING JEWEL of\nHeartlands Institute of Technology; whether\nit be from his INTUITIVE calculator design\nor his contributions to the Skeleton Gang(TM),\nhe's done some impressive work; and that's undisputable.\n")
time.sleep(.3)
print('------------------------------------------------')
print('  What is the "Skeleton Gang"?\n')
time.sleep(.3)
print(" The Skeleton Gang is an organization of\nindividuals where their main goal is to help\nthose in need no matter the situation. We pride\nourselves in our hard work and determination\ntowards completing tasks in a timely manner; as a team.\nWe are the most humble team on the market TO-DATE!")
time.sleep(.1)
print('\n------------------------------------------------')
print("  With all that out of the way, let's get this game going!\n")
time.sleep(.9)
## LET'S GET THIS PARTY STARTED! -= Everything above is simply for a better user experience.

dots = '...'


while True:
    try:
        x = int(input("How many players would you like (1-4):\n"))
        players = x
        single.players = x
        if (x < 1 or x > 4):
            print("Only allowed 1-4 players.\n")
        else:
            break
    except:
        print("That's not a valid number! Choose 1-4.\n")
# While true, ask for an input, if input != a number between 1-4, then repeat question until it does.

time.sleep(.3)
print("\nPreparing", end="")
for i in dots:
    print(i, end="")
    time.sleep(.5)
print("Done!")
time.sleep(.3)
print("Generating word list", end="")
for i in dots:
    print(i, end="")
    time.sleep(.5)
print(f"Done!")
time.sleep(.3)
print("Configurating the thingamajigs", end="")
for i in dots:
    print(i, end="")
    time.sleep(.5)
print(f"Done!\n")
time.sleep(.3)

# Above is more user-oriented things, you can ignore.
if (players == 1):
    importantvars.wordbank
    # Since it's singleplayer, this just throws in a bunch of random words to add to the experience.
    print("GAME SETTINGS: \n")
    print("SINGLEPLAYER ENABLED!")
    print(f"Player Count = {players}")
    print(f"Lives = 6")
    print(f"Difficulty = Normal")
    print(f"Random Words = True")
    print(f"Easter Egg = Hidden")
    print("\nStarting the game", end="")
    for i in dots:
        print(i, end="")
        time.sleep(.5)
    for x in range(100):
        print("\n")
    #clears the screen for the most part, just pushes it all away.

if (players >= 2):
    while True:
        z = input("What would you like the word to be for this game?\n")
        if z.isalpha():
            importantvars.wordbank.append(z)
            break
        if (z.find(" ") > -1):
            print("The word must not contain any spaces!\n")
            continue
        else:
            print("The word must be alphanumeric!\n")
            continue
    print("Word set! Beginning setup. \n\n")
    print("GAME SETTINGS: \n")
    print("MULTIPLAYER MODE!")
    print(f"Player Count = {players}")
    print(f"Lives = 6")
    print(f"Difficulty = Normal")
    print(f"Random Words = True")
    print(f"Easter Egg = Hidden")
    print("\nStarting the game", end="")
    for i in dots:
        print(i, end="")
        time.sleep(.5)
    for x in range(100):
        print("\n")
    #This asks for a user input to add to the list of words, so multiplayer is a little more "hands-on"

# ----==
if (players == 1):
    while True:
        singleplayer()
        if(importantvars.count > 3):
            break # /TimeoutError //1234 wow
        #I wanted the user to be able to repeat the game easily, so any time it prompts them to stop playing it'll add 10 to count if they say no, meaning this loop will break.

if (players == 2):
    while True:
        multi2()
        if(importantvars.count > 3):
            break
        #Same comment as above, only this runs the multiplayer mode (2 plyr).

if (players == 3):
    while True:
        multi3()
        if(importantvars.count > 3):
            break
        #Same comment as above, only this runs the multiplayer mode (3 plyr).

if (players == 4):
    while True:
        multi4()
        if(importantvars.count > 3):
            break
        #Same comment as above, only this runs the multiplayer mode (4 plyr).
