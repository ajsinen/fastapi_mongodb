from pydantic import BaseModel


class ToDoBody(BaseModel):
    title: str
    description: str
