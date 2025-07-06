from app.models.user_model import User
from app.schema.user_schema import UserCreate, UserRead

async def create_user(user_data: UserCreate) -> UserRead:
    user = User(**user_data.model_dump())
    await User.insert_one(user)
    return UserRead(**user.model_dump())