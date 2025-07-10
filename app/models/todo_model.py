from beanie import Document, BeanieObjectId, Indexed
from pydantic import Field
from datetime import datetime
from pytz import timezone


class TodoCategory(Document):
    title: Indexed(str, unique=True)
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



