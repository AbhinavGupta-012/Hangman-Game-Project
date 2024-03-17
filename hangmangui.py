import random
import tkinter as tk

window = tk.Tk()
window.title("Hangman Game")
window.geometry("400x400")
window.configure(bg="grey")
heading = "The Hang Man"

intro = tk.Label(window, text=heading, font=("Helvetica", 18, "bold"), bg="grey", fg="#000000")
intro.place(x=110, y=10)

canvas = tk.Canvas(window, width=200, height=200, bg="grey", borderwidth=0, highlightthickness=0)
canvas.place(x=88, y=88)

def face():
    canvas.create_oval(50, 7, 100, 57, outline="black")

def torso():
    canvas.create_line(75, 60, 75, 110, fill="black")

def left_arm():
    canvas.create_line(52, 105, 72, 70, fill="black")

def right_arm():
    canvas.create_line(78, 70, 100, 105, fill="black")

def left_leg():
    canvas.create_line(52, 145, 72, 110, fill="black")

def right_leg():
    canvas.create_line(78, 110, 100, 145, fill="black")
    
def structure():
    corner = tk.Label(window, text="+", font=("Helvetice", 25, "bold"), bg="grey", fg="brown")
    corner.place(x=150, y=46)
    centre = tk.Label(window, text="---------", font=("Helvetice", 27, "bold"), bg="grey", fg="brown")
    centre.place(x=170, y=41)
    corner_end = tk.Label(window, text="+", font=("Helvetice", 25, "bold"), bg="grey", fg="brown")
    corner_end.place(x=280, y=46)
    stand1 = tk.Label(window, text="|", font=("Helvetica", 25, "bold"), bg="grey", fg="brown")
    stand1.place(x=285, y=77)
    stand2 = tk.Label(window, text="|", font=("Helvetica", 25, "bold"), bg="grey", fg="brown")
    stand2.place(x=285, y=117)
    stand3 = tk.Label(window, text="|", font=("Helvetica", 25, "bold"), bg="grey", fg="brown")
    stand3.place(x=285, y=157)
    stand4 = tk.Label(window, text="|", font=("Helvetica", 25, "bold"), bg="grey", fg="brown")
    stand4.place(x=285, y=197)
    base = tk.Label(window, text="======", font=("Helvetica", 25, "bold"), bg="grey", fg="brown")
    base.place(x=235, y=235)

word = int(random.random()*4)
if word == 1:
    words = "rhino"
elif word == 2:
    words = "hey"
elif word == 3:
    words = "red"
else:
    words = "krishna"

o = []
for i in range(len(words)):
    ab = '_'
    o.append(ab)
hang_man = 0
wrong_words = []

blank_spaces = " ".join("_" * len(words))
word_label = tk.Label(window, text=blank_spaces, font=("Arial", 20), bg="grey")
word_label.place(x=100, y=270)

def display_text():
    text = entry.get()  # Get the text entered by the user
    display_label.config(text=text)

entry = tk.Entry(window, font=("Arial", 12), bg="grey")
entry.place(x=100, y=340)

display_button = tk.Button(window, text="Check", command=display_text, bg="grey", fg="brown")
display_button.place(x=250, y=339)

display_label = tk.Label(window, text=" ", font=("Arial", 12), bg="grey")
display_label.place(x=100, y=270)

for u in range(100):
    guessed = entry.get() 
    if len(guessed) > 1 or len(guessed) < 1:
        more_or_less = tk.Label(window, text="Input should contain only 1 character!", font=("Arial", 12), bg="grey")
        more_or_less.place(x=90, y=370)
        continue
    elif len(guessed) == 0:
        zero = tk.Label(window, text="Input field cannot be left empty!!", font=("Arial", 12), bg="grey")
        zero.place(x=90, y=370)
        continue
    elif guessed in '!@#$%^&*()~`<>/?;:\'"[]|\\=+-_':
        symbol = tk.Label(window, text="Input cannot be a symbol or a special character!!", font=("Arial", 12), bg="grey")
        symbol.place(x=90, y=370)
        continue
    elif guessed in '0123456789':
        number = tk.Label(window, text="Input cannot be a number!", font=("Arial", 12), bg="grey")
        number.place(x=90, y=370)
        continue
    h = guessed.lower()
    if guessed.lower() in words:
        o.pop(words.index(h))
        o.insert(words.index(h), h)
    else:
        wrong_words.append(h)
        hang_man = hang_man + 1
        if hang_man == 1:
            face()
        elif hang_man == 2:
            torso()
        elif hang_man == 3:
            left_arm()
        elif hang_man == 4:
            right_arm()
        elif hang_man == 5:
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

structure()

window.mainloop()