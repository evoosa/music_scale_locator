import pickle
from typing import List

from config import SCALES_TO_INTERVALS, NOTES

OCTAVE = 12


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


def get_scales_containing_note(scales_list: List, note_id: int):
    """ Given a list of scales, get all scales containing a note """
    pass


def get_sorted_scales():
    """ Sort The scales in an efficient way for searching """
    pass


def pickle_data(data, output_file_path: str):
    """ Pickle the sorted data structure of the scales """
    with open(output_file_path, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    pass


def get_scale_notes_names(scale_notes: list):
    """ Get the scale's notes names """
    return [NOTES[i] for i in scale_notes]


if __name__ == '__main__':
    # scale = get_scale(0, SCALES_TO_INTERVALS[1][1])
    # print(scale)
    # print([NOTES[i] for i in scale])
    get_scales()
