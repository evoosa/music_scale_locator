import os
import pickle
import random

from config import NOTES


def pickle_data_if_missing(data, pickle_file_path: str):
    """ Pickle the data structure """
    if not os.path.exists(pickle_file_path):
        with open(pickle_file_path, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print(f'created {pickle_file_path} successfully')
    else:
        print('Scales map file exists, continuing')


def load_pickle_data(pickle_file_path: str):
    """ Pickle the data structure """
    with open(pickle_file_path, 'rb') as pf:
        data = pickle.load(pf)
    return data


def get_scale_notes_names(scale_notes: list):
    """ Get the scale's notes names """
    return [NOTES[i] for i in scale_notes]


def get_random_unicode_music_char():
    """ Get a random unicode musical char """
    music_symbols = [0x1F3B5, 0x1F3B6, 0x1F3BC, 0x1F3B9, 0x1F3BB, 0x1F3B7, 0x1F3B8, 0x1F3BA, 0x1F941, 0x1F399, 0x1F3A4, 0x1F3A7, 0x1F4FB]
    return chr(random.choice(music_symbols))
