from pydantic import BaseModel, EmailStr
from beanie import BeanieObjectId

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
