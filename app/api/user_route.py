"""
    User related endpoints only, separated file for business logic
"""
from fastapi import APIRouter
from app.services.user_service import create_user, authenticate_user
from app.schemas.user_schema import UserCreate, UserLogin
from app.models.user_model import User
from app.schemas.resp_schema import RespModel

user_route = APIRouter(prefix="/users",tags=["Users"])

@user_route.post("/signup")
async def test_todo(request: UserCreate) -> RespModel:
    user_data = await create_user(request)

    return RespModel(message="Success", data=user_data)


@user_route.post("/login")
async def log_in(credential: UserLogin):
    token = await authenticate_user(credential)

    return RespModel(message="Success", data=token)
