from get_scales import get_scales_map


def get_scales_with_note(scales_map: dict, note: int):
    """ Get all scales containing a note from the given scales """
    scales = {scale_name: scales_map[scale_name] for scale_name in scales_map.keys() if note in scales_map[scale_name]}
    return scales


def search_scales(scales_map: dict, notes):
    for note in notes:
        scales_with_note = get_scales_with_note(scales_map, note)
        num_of_scales_with_note = len(scales_with_note)
        if len(notes) == 1:
            print(note, num_of_scales_with_note, scales_with_note)
        else:
            next_iter_notes = list(notes)
            next_iter_notes.remove(note)
            search_scales(scales_with_note, next_iter_notes)


def get_scales_db():
    """ Sort the scales in an efficient way for searching, save it to a file """
    scales_map = get_scales_map()
    print('scales')
    scales = get_scales_with_note(scales_map, 5)
    print(len(scales_map), len(scales), scales)
    # sorted_scales = search_scales(scales_map, range(len(OCTAVE)))


if __name__ == '__main__':
    get_scales_db()
