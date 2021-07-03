OCTAVE = 12

NOTES = [
    'C',
    'C#/Db',
    'D',
    'D#/Eb',
    'E',
    'F',
    'F#/Gb',
    'G',
    'G#/Ab',
    'A',
    'A#/Bb',
    'B'
]

# Intervals between the notes in the scalem in semitones
SCALES_TO_INTERVALS = [
    ('Major', [2, 2, 1, 2, 2, 2]),
    ('Natural Minor', [2, 1, 2, 2, 1, 2]),
    ('Harmonic Minor', [2, 1, 2, 2, 1, 3]),
    ('Ionian', [2, 2, 1, 2, 2, 2]),
    ('Dorian', [2, 1, 2, 2, 2, 1]),
    ('Phyrgian', [1, 2, 2, 2, 1, 2]),
    ('Lydian', [2, 2, 2, 1, 2, 2]),
    ('MixoLydian', [2, 2, 1, 2, 2, 1]),
    ('Aeolian', [2, 1, 2, 2, 1, 2]),
    ('Locrian', [1, 2, 2, 1, 2, 2]),
    ('Pentatonic Major', [2, 2, 3, 2, 3]),
    ('Pentatonic Minor', [3, 2, 2, 3, 2])
]

# GUI
# Colors
LIGHT_GRAPEFRUIT = '#FFCFC4'
MIDTONE_GRAPEFRUIT = '#FFABAB'
DARK_GRAPEFRUIT = '#FF7474'
BROWN = '#560F00'

# Fonts
MAIN_FONT = "Berlin Sans FB"
FONT_TUPLE_TITLE = (MAIN_FONT, 20)
FONT_TUPLE_TEXT = (MAIN_FONT, 15)
