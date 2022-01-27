from tkinter import *
import pandas
import random
#---------------------------------------------------CSV reading-------------------------------------------------------#
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orignal_df = pandas.read_csv("./data/french_words.csv")
    word_dict = orignal_df.to_dict(orient="records")
    current_card = {}
else:
    word_dict = df.to_dict(orient="records")
    current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # The old event is cancelled
    current_card = random.choice(word_dict)
    canvas.itemconfig(change_card, image=card_front_img)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(title_word, text=current_card["French"])
    flip_timer = window.after(3000, flip_card) # new event starts


def flip_card():

    canvas.itemconfig(change_card, image=card_back_img)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(title_word, text=current_card["English"])

#------------------------to make a learn list--------------------------------------------------#
def update_dict():
    word_dict.remove(current_card)
    next_card()
    updated_df = pandas.DataFrame(word_dict)
    updated_df.to_csv("data/words_to_learn.csv",index=False)






# ------------------------------------------------UI Design------------------------------------------------------------#

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("FlashMemory")
window.minsize(width=900, height=800)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
change_card = canvas.create_image(400, 268, image=card_front_img)

canvas.grid(row=0, column=1, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(350, 150, text="title", font=("arial", 20, "italic"))
title_word = canvas.create_text(350, 263, text="word", font=("arial", 30, "bold"))


# Button
# Right Button
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=update_dict)
right_button.grid(row=1, column=2)

# Wrong Button
cross_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()
window.mainloop()

