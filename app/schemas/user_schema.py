from pydantic import BaseModel, EmailStr
from beanie import BeanieObjectId

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class DecodedToken(BaseModel):
    id:BeanieObjectId
    username:str

