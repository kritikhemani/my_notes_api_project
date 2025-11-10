notes = []
note_id_counter = 1

def get_all(skip=0, limit=10):
    return notes[skip: skip + limit]

def get_one(note_id):
    return next((n for n in notes if n["id"] == note_id), None)

def create(note_data):
    global note_id_counter
    note = {
        "id": note_id_counter,
        "title": note_data.title,
        "content": note_data.content
    }
    notes.append(note)
    note_id_counter += 1
    return note

def update(note_id, update_data):
    note = get_one(note_id)
    if note:
        note.update(update_data)
    return note

def delete(note_id):
    note = get_one(note_id)
    if note:
        notes.remove(note)
    return note

