"""
    API endpoints only, separated file for business logic
"""
from fastapi import APIRouter, Depends
from pyexpat.errors import messages

from app.schemas.user_schema import DecodedToken
from app.schemas.todo_schema import ToDoBody, UpdateTodo
from app.schemas.resp_schema import RespModel
from app.core.auth import get_current_user
from app.services.todo_service import TodoService


todo_router = APIRouter(prefix="/todo", tags=["Todos"])


@todo_router.get("/category/list")
async def get_todo_categories():
    category_list = await TodoService.fetch_categories()

    return RespModel(message="Success", data=category_list)


@todo_router.post("/add")
async def create_todo(request: ToDoBody, current_user: DecodedToken = Depends(get_current_user)):
    todo = await TodoService.create_new_todo(current_user, request)

    return RespModel(message="Success", data=todo)


@todo_router.get("/list")
async def fetch_todo_list(current_user: DecodedToken = Depends(get_current_user)) -> RespModel:
    todo_list = await TodoService.get_todo_list(current_user)

    return RespModel(message="Success", data=todo_list)


@todo_router.put("/update/{todo_id}")
async def update_todo_value(todo_id:str, request_body: UpdateTodo,
                            token: DecodedToken = Depends(get_current_user)) -> RespModel:

    updated_record = await TodoService.update_todo(todo_id, token, request_body)

    return RespModel(message="Success", data=updated_record)