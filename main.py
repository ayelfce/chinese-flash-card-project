from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

# ------------------------------ Read Data ---------------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/chinese_words.csv")
    data_dict = original_data.to_dict(orient="records") # to change the dictionary format
else:
    data_dict = data.to_dict(orient="records")


# -------------------------- Known Word -----------------------------


def known_word():
    data_dict.remove(current_card)
    next_card()
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)

# --------------------------- Flip Cards ----------------------------


def flip_card():
    canvas.itemconfig(curr_card, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


# --------------------------- Random Word Func. ---------------------


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    rand_word = current_card["Chinese"]
    canvas.itemconfig(curr_card, image=card_front)
    canvas.itemconfig(language, text="Chinese", fill="black")
    canvas.itemconfig(word, text=rand_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)

# ------------------------------ UI Design ---------------------------


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
curr_card = canvas.create_image(400, 265, image=card_front)
language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 265, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, command=next_card
                   )
wrong_btn.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, command=known_word
                   )
right_btn.grid(column=1, row=1)

next_card()
window.mainloop()
