from typing import Optional
from beanie import BeanieObjectId
from pydantic import BaseModel


class ToDoBody(BaseModel):
    title: str
    description: str
    category_id: str

class UpdateTodo(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None