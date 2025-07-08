from beanie import Document, BeanieObjectId
from pydantic import BaseModel
from datetime import datetime, timezone


class Category(BaseModel):
    name: str
    description: str


class ToDo(Document):
    title: str
    description: str
    created_by: BeanieObjectId
    created_at: datetime = datetime.now(timezone.utc)

    class Settings:
        name = "todos"


