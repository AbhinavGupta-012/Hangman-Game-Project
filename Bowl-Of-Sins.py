import random
import tkinter as tk
from PIL import Image, ImageTk


def toggle_instruction():
    global instructions_open
    if instructions_open:
        frame.pack_forget()
        instructions_open = False
    else:
        frame.pack()
        instructions_open = True


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
    if len(guessed_letter) > 1 and guessed_letter.isalpha():
        display_label.config(text="Invalid Input! Please enter a single letter.")
        return
    elif guessed_letter.isdigit() or (guessed_letter.isdigit() and len(guessed_letter) > 1):
        display_label.config(text="Invalid Input! You cannot enter a number.")
        return
    elif guessed_letter == "":
        display_label.config(text="Input cannot be left empty!")
        return
    elif guessed_letter in "!@#$%^&*()<>/?;:\'\"[]\\" or len(guessed_letter) > 1:
        display_label.config(text="Invalid Input! You cannot enter a symbol.")
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
        entry.config(state="disabled", disabledbackground="#D2B48C")
    if "_" not in displayed_word:
        display_label.config(text="Congratulations! You guessed the word.")
        entry.config(state="disabled", disabledbackground="#D2B48C")


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
window.configure(bg="#D2B48C")

# Load the background image of the bowl
image_path = "C:/Users/Abhinav Gupta/OneDrive/Desktop/Stuff/BowlOfSins.png"
original_image = Image.open(image_path)

# Resize the image
width, height = original_image.size
new_width = 150  # Set the new width here
new_height = int(height * (new_width / width))
resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

# Convert PIL Image to Tkinter PhotoImage
tk_image = ImageTk.PhotoImage(resized_image)

# Create a canvas for drawing circles
canvas3 = tk.Canvas(window, width=resized_image.width, height=resized_image.height, bg="#D2B48C", borderwidth=0, highlightthickness=0, cursor="hand2")
canvas3.place(x=40, y=300)

# Display the image on the canvas
canvas3.create_image(0, 0, anchor=tk.NW, image=tk_image)

# Create labels, entry, and button for hangman game
intro = tk.Button(window, text="Bowl Of Sins", font=("Helvetica", 20, "bold"), command=toggle_instruction, bg="#632A0F", fg="#efae25", borderwidth=2, cursor="hand2")
intro.pack(pady=20)

word_label = tk.Label(window, text=display_word(word, guessed_letters), font=("Arial", 20), bg="#D2B48C")
word_label.place(x=290, y=150)

entry = tk.Entry(window, font=("Arial", 15), bg="#D2B48C")
entry.place(x=240, y=240)

display_button = tk.Button(window, text="Check", font=("Helvetica", 15, "bold"), command=guess_letter, bg="#632A0F", fg="#efae25", cursor="hand2")
display_button.place(x=310, y=280)

display_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="#D2B48C", fg="#632A0F")
display_label.place(x=180, y=200)

instruction_set = tk.Button(window, text="(Press here for instructions)", command=toggle_instruction, font=("Arial", 7, "bold"), bg="#632A0F", fg="#efae25", cursor="hand2", borderwidth=0, highlightthickness=0)
instruction_set.place(x=180, y=57)

instructions_open = False

frame = tk.Frame(window, width=400, height=400, border=2,  highlightbackground="SystemButtonFace")
inst = tk.Canvas(frame,height=350, width=420, bg="#D2B48C")
inst.pack()

inst.create_text(210, 40, text="Instructions", fill="#632A0F", font=("Arial", 20, "bold"))
inst.create_text(210, 80, text="Welcome to Bowl Of Sins", fill="#632A0F", font=("Arial", 16, "bold"))
inst.create_text(200, 120, text="1. You have to guess the word one character at a time.", fill="#632A0F", font=("Arial", 11, "bold"))
inst.create_text(207, 150, text="2. You have infinite tries as long as its the correct guess", fill="#632A0F", font=("Arial", 11, "bold"))
inst.create_text(210, 170, text="but u can only get it wrong 7 times.", fill="#632A0F", font=("Arial", 11, "bold"))

inst.create_text(210, 250, text="ENJOY THE GAME", fill="#632A0F", font=("Arial", 20, "bold"))
window.bind("<Return>", guess_letter)


window.mainloop()
