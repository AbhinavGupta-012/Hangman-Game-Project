import random
import tkinter as tk
from PIL import Image, ImageTk


def draw_circle():
    global circles_count
    x0, y0 = 40, 50
    radius = 8
    spacing = 5
    if circles_count < 4:
        x = x0 + (radius * 2 + spacing) * circles_count
        y = y0
        canvas3.create_oval(x - radius, y - radius, x + radius, y + radius, outline="black", fill="red")
        circles_count += 1
    else:
        x0, y0 = -33, 35
        x = x0 + (radius * 2 + spacing) * circles_count
        y = y0
        canvas3.create_oval(x - radius, y - radius, x + radius, y + radius, outline="black", fill="red")
        circles_count += 1


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
    global coins_count
    display_label.config(text="")
    guessed_letter = entry.get()  # Get the guessed letter
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
        coins_count += 1
        draw_circle()  # Draw a circle in the bowl for each wrong guess
    if coins_count == max_coins:
        display_label.config(text="You lost! The word was: " + word)
        entry.config(state="disabled", disabledbackground="#451b7b")
    if "_" not in displayed_word:
        display_label.config(text="Congratulations! You guessed the word.")
        entry.config(state="disabled", disabledbackground="#451b7b")


# Initialize global variables
word = generate_word()
guessed_letters = set()
coins_count = 0
max_coins = 7
circles_count = 0

# Create the main window
window = tk.Tk()
window.title("Bowl Of Sins")
window.geometry("500x500")
window.configure(bg="#451b7b")

# Load the background image of the bowl
image_path = "/Images/Bowl_Of_Sins.png"
original_image = Image.open(image_path)

# Resize the image
width, height = original_image.size
new_width = 150  # Set the new width here
new_height = int(height * (new_width / width))
resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

# Convert PIL Image to Tkinter PhotoImage
tk_image = ImageTk.PhotoImage(resized_image)

# Create a canvas for drawing circles
canvas3 = tk.Canvas(window, width=resized_image.width, height=resized_image.height, bg="#451b7b", borderwidth=0, highlightthickness=0)
canvas3.place(x=40, y=300)

# Display the image on the canvas
canvas3.create_image(0,      0, anchor=tk.NW, image=tk_image)

# Create labels, entry, and button for hangman game
intro = tk.Label(window, text="Bowl Of Sins", font=("Helvetica", 18, "bold"), bg="#451b7b", fg="#efae25")
intro.pack(pady=20)

word_label = tk.Label(window, text=display_word(word, guessed_letters), font=("Arial", 20), bg="#451b7b")
word_label.place(x=290, y=150)

entry = tk.Entry(window, font=("Arial", 12), bg="#451b7b")
entry.place(x=250, y=240)

display_button = tk.Button(window, text="Check", command=guess_letter, bg="#451b7b", fg="#efae25")
display_button.place(x=400, y=239)

display_label = tk.Label(window, text="", font=("Arial", 12), bg="#451b7b", fg="#efae25")
display_label.place(x=200, y=190)

window.bind("<Return>", guess_letter)

window.mainloop()
