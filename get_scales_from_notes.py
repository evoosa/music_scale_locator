from tkinter import *

from config import NOTES, OCTAVE
from utils import get_random_unicode_music_char

# Colors
LIGHT_GRAPEFRUIT = '#FFCFC4'
LIGHT_GRAPEFRUIT_2 = '#FFABAB'
LIGHT_GRAPEFRUIT_3 = '#FF7474'
BROWN = '#560F00'
FONT_TUPLE = ("Berlin Sans FB", 20)

window = Tk()
window.geometry('800x500')
window.configure(bg=LIGHT_GRAPEFRUIT)

notes_lb = Listbox(window,
                   selectmode="multiple",
                   bg=LIGHT_GRAPEFRUIT,
                   font=FONT_TUPLE,
                   fg=BROWN,
                   width=850, height=10,
                   highlightcolor=LIGHT_GRAPEFRUIT_3,
                   selectbackground=LIGHT_GRAPEFRUIT_3)

notes_lb.pack(expand=YES, fill=NONE, padx=100, pady=10)

for idx in range(OCTAVE):
    line = f'{45 * " "}{get_random_unicode_music_char()}      {NOTES[idx]}{11 * " " if len(NOTES[idx]) == 1 else 3 * " "}   {get_random_unicode_music_char()}{45 * " "}'
    notes_lb.insert(END, line)
    notes_lb.itemconfig(idx, bg=LIGHT_GRAPEFRUIT if idx % 2 == 0 else LIGHT_GRAPEFRUIT_2)


def get_notes_selection():
    return notes_lb.curselection()


# Get Scales Button
Button(window,
       text='Get Scales',
       bg=LIGHT_GRAPEFRUIT_2,
       font=FONT_TUPLE,
       fg=BROWN,
       height=40,
       command=get_notes_selection).pack(padx=50, ipady=7, ipadx=200, pady=20)

window.mainloop()
