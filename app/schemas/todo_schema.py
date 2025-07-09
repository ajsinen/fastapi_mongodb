from typing import Optional

from pydantic import BaseModel


class ToDoBody(BaseModel):
    title: str
    description: str

class UpdateTodo(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None