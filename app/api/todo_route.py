"""
    API endpoints only, separated file for business logic
"""
from fastapi import APIRouter, Depends
from pyexpat.errors import messages

from app.schemas.user_schema import DecodedToken
from app.schemas.todo_schema import ToDoBody
from app.schemas.resp_schema import RespModel
from app.core.auth import get_current_user
from app.services.todo_service import create_new_todo

todo_router = APIRouter(prefix="/todo", tags=["Todos"])


@todo_router.post("/add")
async def create_todo(request: ToDoBody, current_user: DecodedToken = Depends(get_current_user)):
    todo = await create_new_todo(current_user, request)

    return RespModel(message="Success", data=todo)



