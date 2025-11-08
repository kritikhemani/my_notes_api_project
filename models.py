from pydantic import BaseModel, Field
from typing import Optional


class NewNote(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    
class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    content: Optional[str] = Field(None, min_length=1)
    
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str

    