from beanie import Document
from datetime import datetime, timezone

class User(Document):
    username: str
    email: str
    password:str
    created_at: datetime = datetime.now(timezone.utc)

    class Settings:
        name = 'users'