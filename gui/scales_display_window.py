import tkinter as tk
import sys
sys.path.append('..')
from config import NOTES, OCTAVE, LIGHT_GRAPEFRUIT, LIGHT_GRAPEFRUIT_2, LIGHT_GRAPEFRUIT_3, FONT_TUPLE, BROWN


class ScalesDisplayWindow(tk.Toplevel):
    def __init__(self, main_window, *args, **kwargs):
        tk.Toplevel.__init__(self, main_window, *args, **kwargs)
