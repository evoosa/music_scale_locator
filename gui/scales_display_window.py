import sys
import tkinter as tk

sys.path.append('..')
from utils import get_scale_notes_names
from config import NOTES

class ScalesDisplayWindow(tk.Toplevel):
    def __init__(self, main_window, notes: list, scales: dict, *args, **kwargs):
        tk.Toplevel.__init__(self, main_window, *args, **kwargs)
        self.title('  '.join([NOTES[note] for note in notes]))
        self.scales = scales
        self.display_scales_table()

    def display_scales_table(self):
        keys = list(self.scales.keys())
        table_rows = []
        for i in range(len(keys)):
            scale_name = keys[i]
            scale_notes = get_scale_notes_names(self.scales[scale_name])
            scale_notes_formatted = '  '.join(scale_notes)
            current_row = [scale_name, scale_notes]

            name_label = tk.Label(self, text=scale_name, borderwidth=0, width=10)
            name_label.grid(row=i, column=0, sticky="nsew", padx=1, pady=1)
            notes_label = tk.Label(self, text=str(scale_notes_formatted), borderwidth=0, width=10)
            notes_label.grid(row=i, column=1, sticky="nsew", padx=1, pady=1)
            current_row.append(name_label)
            current_row.append(notes_label)
            table_rows.append(current_row)

        for column in range(2):
            self.grid_columnconfigure(column, weight=1)
