from http.client import HTTPException
from fastapi import HTTPException
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def create_user(user_data: UserCreate) ->  User:
    # CHECK IF USERNAME EXISTS
    exists = User.find_one(User.username == user_data.username)
    if exists:
        raise HTTPException(status_code=400, detail="Username already exists")

    user_data.password = hash_password(user_data.password)
    user = User(**user_data.model_dump())

    # INSERT USER TO DATABASE
    await User.insert_one(user)

    return user


async def get_all_user():
    pass
