from fastapi import APIRouter
from zoneinfo import ZoneInfo, available_timezones
from datetime import datetime

healthcheck = APIRouter()


@healthcheck.get("/healthcheck")
async def health_check():
    # print("Avail Timezones", available_timezones())
    now = datetime.now(ZoneInfo("Asia/Manila"))
    print(now)
    return {"status": "TODO is running"}
