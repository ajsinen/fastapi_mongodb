"""
    Business Logics of api are placed here
"""

from app.core.auth import get_current_user
from fastapi import Depends
from app.schemas.user_schema import DecodedToken
from typing import Annotated


async def create_new_todo(token: DecodedToken, request):

    return token.id
