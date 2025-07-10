"""
    Business Logics of api are placed here
"""
from fastapi import HTTPException
from app.schemas.user_schema import DecodedToken
from typing import Annotated
from app.models.todo_model import ToDo, TodoCategory
from app.schemas.todo_schema import ToDoBody, UpdateTodo
from beanie import BeanieObjectId
from bson.errors import InvalidId


class TodoService:
    @staticmethod
    async def create_new_todo(token: DecodedToken, request: ToDoBody):
        todo = ToDo(
            title=request.title,
            description=request.description,
            created_by=token.id
        )
        await ToDo.insert_one(todo)

        return todo


    @staticmethod
    async def get_todo_list(token: DecodedToken) -> list[ToDo]:

        todo_list = await ToDo.find(ToDo.created_by == token.id).to_list()

        return todo_list


    @staticmethod
    async def update_todo(todo_id: str, token: DecodedToken, request_body: UpdateTodo):
        try:
            obj_id = BeanieObjectId(todo_id)
        except(InvalidId, TypeError):
            raise HTTPException(status_code=400, detail="Invalid Input Type")

        # GET_TODO IN DATABASE
        todo = await ToDo.find_one({
            "_id": obj_id,
            "created_by": token.id
        })
        if not todo:
            raise HTTPException(status_code=404, detail="Todo Not Found")

        update_data = request_body.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="Request must not be empty")

        for field, value in update_data.items():
            setattr(todo, field, value)

        await todo.save()

        return todo


    @staticmethod
    async def fetch_categories():
        categories = await TodoCategory.find_all().to_list()

        return categories

