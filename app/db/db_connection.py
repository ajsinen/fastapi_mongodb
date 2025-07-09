from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI
from app.models.user_model import User
from app.models.todo_model import ToDo


async def init_db():

    # CREATE MOTOR CLIENT
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.get_default_database()

    # INITIALIZE BEANIE WITH SAMPLE DOCUMENT CLASS AND DATABASE
    await init_beanie(database=db, document_models=[User, ToDo])