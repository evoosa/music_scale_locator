import tkinter as tk

from .select_notes_window import SelectNotesWindow


def run_gui():
    root = tk.Tk()
    SelectNotesWindow(root).pack()
    root.mainloop()


if __name__ == '__main__':
    run_gui()
