"""
    API endpoints only, separated file for business logic
"""
from fastapi import APIRouter
from app.services.user_service import create_user
from app.schema.user_schema import UserCreate

user_route = APIRouter(prefix="/users",tags=["Users"])

@user_route.post("/todo/test")
async def test_todo(request: UserCreate):
    return await create_user(request)