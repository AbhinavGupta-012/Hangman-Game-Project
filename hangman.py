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
for u in range(100):
    s = input("\nGuess A Word: ")
    if (len(s) > 1 or len(s) < 1):
        print("Input should contain only 1 character!")
        continue
    elif (len(s) == 0):
        print("Input field cannot be left empty!!")
        continue
    elif (s in '!@#$%^&*()~`<>/?;:\'"[]|\\=+-_'):
        print("Input cannot be a symbol or a special character!!")
        continue
    elif (s in '0123456789'):
        print("Input cannot be a number!")
        continue
    h = s.lower()
    if s.lower() in words:
        o.pop(words.index(h))
        o.insert(words.index(h), h)
    else:
        wrong_words.append(h)   
        hang_man = hang_man + 1
        if(hang_man == 1):
            face()
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
