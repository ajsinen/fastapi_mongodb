from beanie import Document, BeanieObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from pytz import timezone
from zoneinfo import ZoneInfo


class TodoCategory(Document):
    title: str
    description: str
    created_at: datetime = datetime.now(timezone("Asia/Manila"))

    class Settings:
        name = "todo_categories"


class ToDo(Document):
    title: str
    description: str
    created_by: BeanieObjectId
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone("Asia/Manila"))
    )

    class Settings:
        name = "todos"



