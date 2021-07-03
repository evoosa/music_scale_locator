from tkinter import *

from config import NOTES, OCTAVE
from utils import get_random_unicode_music_char
from create_scales_db import get_scales_for_notes_from_db

# from get_scales_db import
# Colors
LIGHT_GRAPEFRUIT = '#FFCFC4'
MIDTONE_GRAPEFRUIT = '#FFABAB'
DARK_GRAPEFRUIT = '#FF7474'
BROWN = '#560F00'
FONT_TUPLE = ("Berlin Sans FB", 20)


def run_note_selection():
    """ Run GUI for the user to choose notes """
    root_window = Tk()
    root_window.geometry('800x500')
    root_window.configure(bg=LIGHT_GRAPEFRUIT)

    # Create select notes list box
    notes_lb = Listbox(root_window,
                       selectmode="multiple",
                       bg=LIGHT_GRAPEFRUIT,
                       font=FONT_TUPLE,
                       fg=BROWN,
                       width=850, height=10,
                       highlightcolor=DARK_GRAPEFRUIT,
                       selectbackground=DARK_GRAPEFRUIT)

    notes_lb.pack(expand=YES, fill=NONE, padx=100, pady=10)

    # Create elements in checkbox
    for idx in range(OCTAVE):
        line = f'{45 * " "}{get_random_unicode_music_char()}      {NOTES[idx]}{11 * " " if len(NOTES[idx]) == 1 else 3 * " "}   {get_random_unicode_music_char()}{45 * " "}'
        notes_lb.insert(END, line)
        notes_lb.itemconfig(idx, bg=LIGHT_GRAPEFRUIT if idx % 2 == 0 else MIDTONE_GRAPEFRUIT)

    def create_window():
        window = Toplevel(root_window)

    # Create Get Scales Button
    def display_scales_for_note_selection():
        notes = notes_lb.curselection()
        scales = get_scales_for_notes_from_db(notes)
        create_window()
        return

    Button(root_window,
           text='Get Scales',
           bg=MIDTONE_GRAPEFRUIT,
           font=FONT_TUPLE,
           fg=BROWN,
           command=display_scales_for_note_selection).pack(padx=50, ipady=7, ipadx=200, pady=20)

    root_window.mainloop()


if __name__ == '__main__':
    run_note_selection()
