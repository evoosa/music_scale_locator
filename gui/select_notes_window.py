import sys
import tkinter as tk

sys.path.append('..')
from config import NOTES, OCTAVE, LIGHT_GRAPEFRUIT, LIGHT_GRAPEFRUIT_2, LIGHT_GRAPEFRUIT_3, FONT_TUPLE, BROWN
from utils import get_random_unicode_music_char
from create_scales_db import get_scales_for_notes_from_db
from scales_display_window import ScalesDisplayWindow


class SelectNotesWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self._configure_parent()
        self.notes_lb = tk.Listbox(self.parent, selectmode="multiple")
        self._configure_lb()
        self.scales_button = tk.Button(self.parent)
        self._configure_button()

    def _configure_parent(self):
        self.parent.geometry('800x500')
        self.parent.title("Notes Selection")
        self.parent.configure(bg=LIGHT_GRAPEFRUIT)

    def _configure_lb(self):
        """ Configure the notes list box """
        self.notes_lb.config(bg=LIGHT_GRAPEFRUIT,
                             font=FONT_TUPLE,
                             fg=BROWN,
                             width=850, height=OCTAVE,
                             highlightcolor=LIGHT_GRAPEFRUIT_3,
                             selectbackground=LIGHT_GRAPEFRUIT_3)
        self.notes_lb.pack(expand=tk.YES, fill=tk.NONE, padx=100, pady=10)

        # Create the list of notes buttons
        for idx in range(OCTAVE):
            line = f'{30 * " "}{get_random_unicode_music_char()}      {NOTES[idx]}{11 * " " if len(NOTES[idx]) == 1 else 3 * " "}   {get_random_unicode_music_char()}{45 * " "}'
            self.notes_lb.insert(tk.END, line)
            self.notes_lb.itemconfig(idx, bg=LIGHT_GRAPEFRUIT if idx % 2 == 0 else LIGHT_GRAPEFRUIT_2)

    def _configure_button(self):
        """ Configure the button """
        self.scales_button.config(text='Get Scales',
                                  bg=LIGHT_GRAPEFRUIT_2,
                                  font=FONT_TUPLE,
                                  fg=BROWN,
                                  command=self.button_click)
        self.scales_button.pack(padx=50, ipady=7, ipadx=200, pady=20)

    def button_click(self):
        notes = self.notes_lb.curselection()
        scales = get_scales_for_notes_from_db(notes)
        print(scales)
        ScalesDisplayWindow(self)


if __name__ == "__main__":
    root = tk.Tk()
    SelectNotesWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
