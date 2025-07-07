from beanie import Document, Indexed, BeanieObjectId
from pydantic import BaseModel
from datetime import datetime, timezone

class Category(BaseModel):
    name: str
    description: str

class ToDo(Document):
    id: BeanieObjectId
    title: str
    description: str
    created_by: str
    created_at: datetime = datetime.now(timezone.utc)


