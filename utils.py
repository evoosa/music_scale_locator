import pickle

from playGround.MusicScaleLocator.config import NOTES


def pickle_data(data, output_file_path: str):
    """ Pickle the sorted data structure of the scales """
    with open(output_file_path, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    pass


def get_scale_notes_names(scale_notes: list):
    """ Get the scale's notes names """
    return [NOTES[i] for i in scale_notes]