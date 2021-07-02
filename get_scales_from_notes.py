# get the notes
# get the db
# set the input, list it and repr
# get the scales from the DB

# from tkinter import Tk, Listbox, YES, END, NO
from tkinter import *
from utils import get_random_unicode_music_char
from config import NOTES, OCTAVE

# Colors
GREY = '#676767'
LIGHT_GRAPEFRUIT = '#FFCFC4'
LIGHT_GRAPEFRUIT_2 = '#FFABAB'
LIGHT_GRAPEFRUIT_3 = '#FF7474'
BROWN = '#560F00'
FONT_TUPLE = ("Berlin Sans FB", 20)

window = Tk()
window.geometry('800x800')

# Choosing selectmode as multiple
# for selecting multiple options
notes = Listbox(window,
                selectmode="multiple",
                bg=LIGHT_GRAPEFRUIT,
                font=FONT_TUPLE,
                fg=BROWN,
                width=850, height=180,
                highlightcolor=LIGHT_GRAPEFRUIT_3,
                selectbackground=LIGHT_GRAPEFRUIT_3)

# Widget expands horizontally and
# vertically by assigning both to
# fill option
notes.pack(expand=YES, fill=NONE, padx=5, pady=5)

# Taking a list 'x' with the items
# as languages
x = ["C", "C++", "Java", "Python", "R",
     "Go", "Ruby", "JavaScript", "Swift"]

for idx in range(OCTAVE):
    line = f'{45 * " "}{get_random_unicode_music_char()}      {NOTES[idx]}{11 * " " if len(NOTES[idx]) == 1 else 3 * " "}   {get_random_unicode_music_char()}{45 * " "}'
    notes.insert(END, line)
    notes.itemconfig(idx,
                     bg=LIGHT_GRAPEFRUIT if idx % 2 == 0 else LIGHT_GRAPEFRUIT_2,

                     )

window.mainloop()
