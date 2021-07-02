import os

from config import SCALES_TO_INTERVALS, NOTES
from utils import pickle_data, get_scale_notes_names

OCTAVE = 12
SCALES_MAP_FILE = 'scales_map.pickle'


def get_scales():
    """ Get all the scales """
    scales = {}
    for note in range(OCTAVE):
        note_name = NOTES[note]
        for scale_type in SCALES_TO_INTERVALS:
            scale_name = f'{note_name} {scale_type[0]}'
            scale = get_scale(note, scale_type[1])
            scales[scale_name] = scale
            print(scale_name, get_scale_notes_names(scale))
    print(f'Total of {len(scales)} scales')
    return scales


def get_scale(tonic: int, scale_intervals: list):
    """ Get the scale's notes given his tonic and it's intervals """
    scale_notes = [tonic]
    current_note = tonic
    for interval in scale_intervals:
        current_note = (current_note + interval) % OCTAVE
        scale_notes.append(current_note)
    return scale_notes


def main():
    """ Create Scales DB """
    if not os.path.exists(SCALES_MAP_FILE):
        scales = get_scales()
        pickle_data(scales, SCALES_MAP_FILE)
        print('created scales map file successfully')
    else:
        print('Scales map file exists, continuing')


if __name__ == '__main__':
    main()
