from datetime import datetime, timedelta
from jose import jwt
from server.src.core.config import settings


def create_token(data: dict, expires_timedelta: timedelta):
    print("Creating token with data:", data)
    payload = data.copy()
    expire = datetime.utcnow() + expires_timedelta
    payload.update(
        {
            "sub": str(data["sub"]),
            "owner": str(data["owner"]),
            "exp": expire,
        }
    )
    encoded_jwt = jwt.encode(
        payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def create_access_token(data: dict):
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return create_token(data, access_token_expires)


def create_refresh_token(data: dict):
    refresh_token_expires = timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )
    return create_token(data, refresh_token_expires)
