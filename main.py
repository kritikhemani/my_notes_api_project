from fastapi import FastAPI, Depends
import database
from models import NewNote, NoteUpdate, NoteResponse


app = FastAPI(title="Notes API")

def get_db():
    return database

@app.post("/notes/", response_model=NoteResponse)
def create_note(note: NewNote, db=Depends(get_db)):
    return db.create(note)