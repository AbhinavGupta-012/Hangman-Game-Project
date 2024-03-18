import random
import tkinter as tk

window = tk.Tk()
window.title("Hangman Game")
window.geometry("400x400")
window.configure(bg="grey")

intro = tk.Label(window, text="The Hang Man", font=("Helvetica", 18, "bold"), bg="grey", fg="#000000")
intro.place(x=110, y=10)

canvas = tk.Canvas(window, width=200, height=200, bg="grey", borderwidth=0, highlightthickness=0)
canvas.place(x=88, y=88)


def draw_hangman(part):
    if part == "head":
        canvas.create_oval(50, 7, 100, 57, outline="black")
    elif part == "torso":
        canvas.create_line(75, 60, 75, 110, fill="black")
    elif part == "left_arm":
        canvas.create_line(52, 105, 72, 70, fill="black")
    elif part == "right_arm":
        canvas.create_line(78, 70, 100, 105, fill="black")
    elif part == "left_leg":
        canvas.create_line(52, 145, 72, 110, fill="black")
    elif part == "right_leg":
        canvas.create_line(78, 110, 100, 145, fill="black")


def structure():
    corner = tk.Label(window, text="+", font=("Helvetica", 25, "bold"), bg="grey", fg="brown")
    corner.place(x=150, y=46)
    centre = tk.Label(window, text="---------", font=("Helvetica", 27, "bold"), bg="grey", fg="brown")
    centre.place(x=170, y=41)
    corner_end = tk.Label(window, text="+", font=("Helvetica", 25, "bold"), bg="grey", fg="brown")
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


def generate_word():
    words = ["rhino", "hey", "red", "krishna"]
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def guess_letter(event=None):
    display_label.config(text="")
    guessed_letter = entry.get()
    if len(guessed_letter) != 1 or not guessed_letter.isalpha():
        display_label.config(text="Invalid input! Please enter a single letter.")
        return
    guessed_letter = guessed_letter.lower()
    if guessed_letter in guessed_letters:
        display_label.config(text="You have already guessed this letter.")
        return
    guessed_letters.add(guessed_letter)
    displayed_word = display_word(word, guessed_letters)
    word_label.config(text=displayed_word)
    if guessed_letter not in word:
        wrong_letters.append(guessed_letter)
        draw_hangman(parts[wrong_letters.index(guessed_letter)])
    if len(wrong_letters) == len(parts):
        display_label.config(text="You lost! The word was: " + word)
        entry.config(state="disabled", disabledbackground="grey", disabledforeground="black")
    if "_" not in displayed_word:
        display_label.config(text="Congratulations! You have Guessed the word!")
        display_label.place(x=40, y=310)
        entry.config(state="disabled", disabledbackground="grey", disabledforeground="black")


def delete_button(button):
    button.destroy()
    structure()


word = generate_word()
guessed_letters = set()
wrong_letters = []
parts = ["head", "torso", "left_arm", "right_arm", "left_leg", "right_leg"]

word_label = tk.Label(window, text=display_word(word, guessed_letters), font=("Arial", 20), bg="grey")
word_label.place(x=100, y=270)

entry = tk.Entry(window, font=("Arial", 12), bg="grey")
entry.place(x=100, y=340)

display_button = tk.Button(window, text="Check", command=guess_letter, bg="grey", fg="brown")
display_button.place(x=250, y=339)

display_label = tk.Label(window, text="", font=("Arial", 12), bg="grey")
display_label.place(x=100, y=310)

start = tk.Button(window, text="PLAY", font=("Arial", 15, "bold"), command=lambda: delete_button(start), bg="grey", fg="white", height=13, width=29)
start.place(x=20, y=50)

window.bind("<Return>", guess_letter)

window.mainloop()
