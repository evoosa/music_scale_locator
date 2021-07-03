import os

from config import SCALES_TO_INTERVALS, NOTES, OCTAVE
from utils import pickle_data_if_missing, load_pickle_data

SCALES_DB_FILE = 'scales_db.pickle'
scales_db = {}


def get_all_scales():
    """ Get all scales """
    scales = {}
    for note in range(OCTAVE):
        note_name = NOTES[note]
        for scale_type in SCALES_TO_INTERVALS:
            scale_name = f'{note_name} {scale_type[0]}'
            scale = get_scale_from_tonic(note, scale_type[1])
            scales[scale_name] = scale
    print(f'Total of {len(scales)} scales')
    return scales


def get_scale_from_tonic(tonic: int, intervals: list):
    """ Get the scale's notes given his tonic and it's intervals """
    scale_notes = [tonic]
    current_note = tonic
    for interval in intervals:
        current_note = (current_note + interval) % OCTAVE
        scale_notes.append(current_note)
    return scale_notes


def get_scales_containing_note(scales_map: dict, note: int):
    """ Get all scales containing a note from the given scales """
    scales = {scale_name: scales_map[scale_name] for scale_name in scales_map.keys() if note in scales_map[scale_name]}
    return scales


def create_scales_db(ancestor_notes: list, scales_map: dict, notes):
    """ Create the map between note sets, and the scales containing them """
    for note in notes:
        # Get the notes for the next iteration
        next_iter_ancestor_notes = list(ancestor_notes)
        next_iter_ancestor_notes.append(note)
        # Get the key to update the scale map with
        key_elements = list(next_iter_ancestor_notes)
        key_elements.sort()
        key = repr(key_elements)
        # If the key is missing, get the scales corresponding to the given notes and update the scale map
        if key not in scales_db:
            scales_with_note = get_scales_containing_note(scales_map, note)
            scales_db[key] = scales_map
            if not ((len(scales_with_note) == 0) or (len(notes) == 1)):
                next_iter_notes = list(notes)
                next_iter_notes.remove(note)
                create_scales_db(next_iter_ancestor_notes, scales_with_note, next_iter_notes)


def create_and_load_db():
    """ Sort the scales in an efficient way for searching, save it to a file, and load it """
    if not os.path.exists(SCALES_DB_FILE):
        scales_map = get_all_scales()
        create_scales_db([], scales_map, list(range(OCTAVE)))
        pickle_data_if_missing(scales_db, SCALES_DB_FILE)
        return scales_db
    else:
        return load_pickle_data(SCALES_DB_FILE)


def get_scales_for_notes_from_db(notes: list):
    """ Get the scales for the given notes from the DB """
    scales_db = create_and_load_db()
    notes = list(set(notes))
    notes.sort()
    key = repr(notes)
    try:
        scales = scales_db[key]
    except Exception as e:
        print (f'ERROR: {e}')
        return 'Error Sorry :<'
    return scales


if __name__ == '__main__':
    test_notes = [1, 4, 7, 3, 3]
    get_scales_for_notes_from_db(test_notes)
