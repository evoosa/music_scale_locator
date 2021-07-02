from typing import List

from config import SCALES_TO_INTERVALS, NOTES

OCTAVE = 12


def get_scales():
    """ Get all the scales """
    # for i in range(OCTAVE):

    pass


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


def pickle_sorted_scales():
    """ Pickle the sorted data structure of the scales """
    pass


if __name__ == '__main__':
    scale = get_scale(0, SCALES_TO_INTERVALS[2][1])
    print(scale)
    print([NOTES[i] for i in scale])
