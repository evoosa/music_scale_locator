# MusicScaleLocator

Locates all scales containing a set of notes of the user's choice
- [ !!! ] If you find any bugs please comment them! :)

# Backend

It was important to me to avoid creating + searching the scale DB again and again in each run, so the script will create a sorted chords DB at the beginning of the run
- The DB is stored in a pickle file in this directory
``` 
scales_db.pickle
```

# Usage
It's a GUI program. activate it by running:
``` 
python3 main.py
``` 

# Environment
- *Python Version*
    - I used python3.9

- *OS*
    - Windows

- *Packages*
    - All of them are built-in
    - Tkinter, pickle, random

# TODO
- add description for the scales, including the mood
- turn to a python package / .exe file