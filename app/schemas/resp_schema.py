from typing import Optional, Generic, TypeVar, Any
from pydantic import BaseModel, ConfigDict


class RespModel(BaseModel):
    message:str
    data: Optional[Any] = None

