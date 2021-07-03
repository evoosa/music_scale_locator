import sys
import tkinter as tk

sys.path.append('..')
from utils import get_scale_notes_names
from config import NOTES, LIGHT_GRAPEFRUIT, LIGHT_GRAPEFRUIT_2, BROWN, FONT_TUPLE_TEXT


class ScalesDisplayWindow():
    def __init__(self, notes: list, scales: dict, *args, **kwargs):
        self.parent = tk.Toplevel()
        self.notes = notes
        self.scales = scales
        self._configure_window()
        self.canvas = tk.Canvas(self.parent)
        self.scroll_y = tk.Scrollbar(self.parent, orient="vertical", command=self.canvas.yview)
        self.frame = tk.Frame(self.canvas)
        # self.frame

        self.display_scales_table()
        self._configure_canvas()
        self._configure_scrollbar()

    def _configure_canvas(self):
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'),
                              yscrollcommand=self.scroll_y.set,
                              bg=LIGHT_GRAPEFRUIT)
        self.canvas.pack(fill='both', expand=True, side='left', padx=50, pady=10)

    def _configure_scrollbar(self):
        self.scroll_y.pack(fill='y', side='right')

    def _configure_window(self):
        self.parent.geometry('860x600')
        self.parent.title(f'Scales For Notes: {"  ".join([NOTES[note] for note in self.notes])}')
        self.parent.configure(bg=LIGHT_GRAPEFRUIT)

    def display_scales_table(self):
        keys = list(self.scales.keys())
        for i in range(len(keys)):
            scale_name = keys[i]
            scale_notes = get_scale_notes_names(self.scales[scale_name])
            scale_notes_formatted = f"    {'   '.join(scale_notes)}"
            name_label = tk.Label(self.frame, width=25)
            self._configure_label(name_label, scale_name, i, 0)
            notes_label = tk.Label(self.frame, anchor="w", width=39)
            self._configure_label(notes_label, scale_notes_formatted, i, 1)
        self.canvas.grid_columnconfigure(0, weight=1)
        self.canvas.grid_columnconfigure(1, weight=1)

    @staticmethod
    def _configure_label(label, text, row, column):
        label.config(text=text,
                     borderwidth=5,
                     bg=LIGHT_GRAPEFRUIT if row % 2 == 0 else LIGHT_GRAPEFRUIT_2,
                     fg=BROWN,
                     font=FONT_TUPLE_TEXT,
                     )
        label.grid(row=row,
                   column=column,
                   sticky='nesw',
                   padx=2,
                   pady=2,
                   ipady=10)
