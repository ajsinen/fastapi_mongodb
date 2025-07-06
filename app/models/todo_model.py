from beanie import Document, Indexed
from pydantic import BaseModel

class Category(BaseModel):
    name: str
    description: str

class ToDo(Document):
    title: str
    description: str


