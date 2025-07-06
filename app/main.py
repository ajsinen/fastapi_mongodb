from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.todo_route import todo_router
from app.api.user_route import user_route
from app.db.db_connection import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing DB connection")
    await init_db()
    yield
    print("Shutting down...")

app = FastAPI(
    title="Todo list using Mongodb",
    lifespan=lifespan
)

app.include_router(todo_router)
app.include_router(user_route)