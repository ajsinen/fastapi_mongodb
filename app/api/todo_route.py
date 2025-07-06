from fastapi import APIRouter

"""
    API endpoints only, separated file for business logic
"""


todo_router = APIRouter(prefix="/todo")

@todo_router.get("/todo/test")
async def test_todo():
    return {"message": "todo endpoints"}