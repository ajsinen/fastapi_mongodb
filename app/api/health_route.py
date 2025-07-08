from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/")
async def health_check():
    return {"message": "service is running"}