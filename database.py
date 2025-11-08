notes = []
note_id_counter = 1

def get_all(skip=0, limit=10):
    return notes[skip: skip + limit]