from tkinter import *
from PIL import Image, ImageTk
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#-------------------------------------UI Part-------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#Canvas
canvas = Canvas(width= 500, height=300, highlightthickness=0)

#Front image settings
front_image = Image.open("./images/card_front.png")
front_image = front_image.resize((500,300))
front_image = ImageTk.PhotoImage(front_image)

#Back image settings
back_image = Image.open("./images/card_back.png")
back_image = back_image.resize((500,300))
back_image = ImageTk.PhotoImage(back_image)

card_background = canvas.create_image(250,150,image=front_image)

card_title = canvas.create_text(250, 100, text="", font=("Ariel", 20, "italic"))
card_word = canvas.create_text(250, 175, text="", font=("Ariel", 30, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2 )

#Button
tick_image  = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=next_card)
tick_button.grid(row=1, column=1)
cross_image = PhotoImage(file="./images/wrong.png")
cross_button =Button(image=cross_image, highlightthickness=0, command=is_known)
cross_button.grid(row=1, column=0)

next_card()

window.mainloop()