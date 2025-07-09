from beanie import Document, BeanieObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from pytz import timezone
from zoneinfo import ZoneInfo


class Category(BaseModel):
    name: str
    description: str


class ToDo(Document):
    title: str
    description: str
    created_by: BeanieObjectId
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone("Asia/Manila"))
    )

    class Settings:
        name = "todos"


