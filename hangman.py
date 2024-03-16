import random

#printing the Hangman
def face():
    print("\t\t\t+-----------+")    
    print("\t\t\tO\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t             ======")


def neck():
    print("\t\t\t+-----------+")    
    print("\t\t\tO\t|")
    print("\t\t\t|\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t             ======")


def left_hand():
    print("\t\t\t+-----------+")    
    print("\t\t\tO\t|")
    print("\t\t       /|\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t             ======")


def right_hand():
    print("\t\t\t+-----------+")    
    print("\t\t\tO\t|")
    print("\t\t       /|\\\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t             ======")


def left_leg():
    print("\t\t\t+-----------+")    
    print("\t\t\tO\t|")
    print("\t\t       /|\\\t|")
    print("\t\t       /\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t             ======")


def right_leg():
    print("\t\t\t+-----------+")    
    print("\t\t\tO\t|")
    print("\t\t       /|\\\t|")
    print("\t\t       / \\\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t             ======")


#structure of hanging
def structure():
    print("\t\t\t+-----------+")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t\t|")
    print("\t\t\t             ======")


#defining the words using random
word = int(random.random()*4)
if word == 1:
    words = "rhino"
elif word == 2:
    words = "hey"
elif word == 3:
    words = "red"
else:
    words = "krishna"

#creating a block of underscores of length of the given word
o = []
for i in range(len(words)):
    ab = '_'
    o.append(ab)
hang_man = 0

#2nd Version
#PRINTING THE SET OF INSTRUCTIONS
print("THE HANGMAN")
print("# Some Words are prefixed and you have to guess them.")
print("# If the guessed word is correct, then the blank is replaced by the word!")
print("# Otherwise your chances are reduced (Maximum Wrong Guesses: 6)")
#printing the block of underscores
structure()

for i in o:
    print(i, end=' ')

wrong_words = []

#playing the real game 
for u in range(len(words) + 6):
    s = input("\nGuess A Word: ")
    for t in s:
        if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            right_leg()
            print('You Are Terminated')
            break
    if s in words:
        o.pop(words.index(s))
        o.insert(words.index(s), s)
    else:
        wrong_words.append(s)
        hang_man = hang_man + 1
        if(hang_man == 1):
            face()
            wrong_words.append(s)
        elif(hang_man == 2):
            neck()
        elif(hang_man == 3):
            left_hand()
        elif(hang_man == 4):
            right_hand()
        elif(hang_man == 5):
            left_leg()
        else:
            right_leg()
            print("YOU ARE TERMINATED")
            break
    for i in wrong_words:
            print(i, end='  ')
    print('\n')
    for i in o:
        print(i, end="  ")
    if '_' not in o:
        print("\nCongratulations! You Have Completed the Game")
        break
    