from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_FILE = r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day31-flash-card-app-capstone\images\card_front.png"
CARD_BACK_FILE =  r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day31-flash-card-app-capstone\images\card_back.png"

# --------------------------- DATA ------------------------------------

try:
    data = pd.read_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day31-flash-card-app-capstone\data\words_to_learn.csv")
    if len(data.to_dict(orient="records")) == 0:
        data = pd.read_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day31-flash-card-app-capstone\data\most_common_english_words_to_spanish.csv")
except:
    data = pd.read_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day31-flash-card-app-capstone\data\most_common_english_words_to_spanish.csv")

to_learn = data.to_dict(orient="records")
current_card = {}

# ----------------------------- UI ------------------------------------


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfigure(img, image=front_card_img)
    canvas.itemconfigure(card_title, text="English", fill="black")
    canvas.itemconfigure(word_text, text=current_card["English"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfigure(img, image=back_card_img)
    canvas.itemconfigure(card_title, text="Español", fill="white")
    canvas.itemconfigure(word_text, text=current_card["Spanish"], fill="white")

def delete_word():
    global current_card
    to_learn.remove(current_card)
    pd.DataFrame.from_dict(to_learn).to_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day31-flash-card-app-capstone\data\words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_img = PhotoImage(file=CARD_FRONT_FILE)
back_card_img = PhotoImage(file=CARD_BACK_FILE)
img = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"))

current_card = choice(to_learn)

word_text = canvas.create_text(400, 263, text=current_card["English"], font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


wrong_button_img = PhotoImage(file=r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day31-flash-card-app-capstone\images\wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file=r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day31-flash-card-app-capstone\images\right.png")
right_button = Button(image=right_button_img, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR, command=delete_word)
right_button.grid(column=1, row=1)

window.mainloop()
