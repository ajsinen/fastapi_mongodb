from os import access
from os.path import exists
from app.core.security import hash_password,verify_password, create_access_token
from fastapi import HTTPException
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserLogin, TokenResponse
from passlib.hash import argon2


async def create_user(user_data: UserCreate) ->  User:
    # CHECK IF USERNAME EXISTS
    existing = await User.find_one(User.username == user_data.username)
    print(exists)
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    user_data.password = hash_password(user_data.password)
    user = User(**user_data.model_dump())

    # INSERT USER TO DATABASE
    await User.insert_one(user)

    return user


async def authenticate_user(credentials: UserLogin) -> TokenResponse:
    # CHECK IF USERNAME EXISTS
    user = await User.find_one(User.username == credentials.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # CHECK IF PASSWORD IS VALID
    if not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_data = {
        "sub": str(user.id),
        "username": user.username
    }

    token = create_access_token(token_data)
    data = TokenResponse(
        access_token=token
    )
    return data