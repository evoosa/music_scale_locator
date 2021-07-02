import os
import pickle

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
