import sys
import tkinter as tk

sys.path.append('..')
from utils import get_scale_notes_names
from config import NOTES, LIGHT_GRAPEFRUIT, LIGHT_GRAPEFRUIT_2, LIGHT_GRAPEFRUIT_3


class ScalesDisplayWindow(tk.Toplevel):
    def __init__(self, main_window, notes: list, scales: dict, *args, **kwargs):
        tk.Toplevel.__init__(self, main_window, *args, **kwargs)
        self.notes = notes
        self.scales = scales
        self._configure_window()

        self.canvas = tk.Canvas(self)
        self.scroll_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.frame = tk.Frame(self.canvas)

        self.display_scales_table()
        self._configure_canvas()
        self._configure_scrollbar()

    def _configure_canvas(self):
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scroll_y.set)
        self.canvas.pack(fill='both', expand=True, side='left')

    def _configure_scrollbar(self):
        self.scroll_y.pack(fill='y', side='right')

    def _configure_window(self):
        self.geometry('800x500')
        self.title(f'Scales For Notes: {"  ".join([NOTES[note] for note in self.notes])}')
        self.configure(bg=LIGHT_GRAPEFRUIT_3)

    def display_scales_table(self):
        keys = list(self.scales.keys())
        for i in range(len(keys)):
            scale_name = keys[i]
            scale_notes = get_scale_notes_names(self.scales[scale_name])
            scale_notes_formatted = '  '.join(scale_notes)
            name_label = tk.Label(self.frame)
            self._configure_label(name_label, scale_name, i, 0)
            notes_label = tk.Label(self.frame)
            self._configure_label(notes_label, scale_notes_formatted, i, 1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    @staticmethod
    def _configure_label(label, text, row, column):
        label.config(text=text,
                     borderwidth=5, width=50,
                     bg=LIGHT_GRAPEFRUIT if row % 2 == 0 else LIGHT_GRAPEFRUIT_2,
                     )
        label.grid(row=row, column=column, sticky='nesw', padx=1, pady=1)
