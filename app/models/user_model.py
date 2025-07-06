from beanie import Document

class User(Document):
    username: str
    email: str

    class Settings:
        name = 'users'