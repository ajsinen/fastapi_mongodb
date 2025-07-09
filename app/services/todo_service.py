"""
    Business Logics of api are placed here
"""
from app.schemas.user_schema import DecodedToken
from typing import Annotated
from app.models.todo_model import ToDo
from app.schemas.todo_schema import ToDoBody


async def create_new_todo(token: DecodedToken, request: ToDoBody):
    todo = ToDo(
        title=request.title,
        description=request.description,
        created_by=token.id
    )
    await ToDo.insert_one(todo)

    return todo


async def get_todo_list(token: DecodedToken) -> list[ToDo]:

    todo_list = await ToDo.find(ToDo.created_by == token.id).to_list()
    print("TODO LIST",todo_list)
    return todo_list
