"""
    User related endpoints only, separated file for business logic
"""
from fastapi import APIRouter
from app.services.user_service import create_user, get_all_user
from app.schemas.user_schema import UserCreate
from app.models.user_model import User
from app.schemas.resp_schema import RespModel

user_route = APIRouter(prefix="/users",tags=["Users"])

@user_route.post("/signup")
async def test_todo(request: UserCreate):
    user_data = await create_user(request)

    return RespModel(message="Success", data=user_data)
