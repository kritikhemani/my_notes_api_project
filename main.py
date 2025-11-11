from fastapi import FastAPI, Depends, HTTPException
from typing import List
import database
from models import NewNote, NoteUpdate, NoteResponse


app = FastAPI(title="Notes API")

def get_db():
    return database

@app.post("/notes/", response_model=NoteResponse)
def create_note(note: NewNote, db=Depends(get_db)):
    return db.create(note)

@app.get("/notes/", response_model=List[NoteResponse])
def read_notes(skip: int = 0, limit: int = 10, db=Depends(get_db)):
    return db.get_all(skip, limit)

@app.get("/notes/{note_id}", response_model=NoteResponse)
def read_notes(note_id: int, db=Depends(get_db)):
    note = db.get_one(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note