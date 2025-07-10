from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
from dotenv import load_dotenv
import os
import re

load_dotenv()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def is_valid_password(password: str) -> bool:
    """
    Validates whether the password contains:
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one digit
    - at least one special character
    """
    if len(password) < 8:
        return False

    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[!@#$%^&*()_\-+=\[\]{};:'\"\\|,.<>/?]", password)

    return all([has_upper, has_lower, has_digit, has_special])


def create_access_token(data: dict, expires_delta: timedelta | None = None):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
