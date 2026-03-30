from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.login.schemas.login_schema import UserLogin
from server.src.login.services.login_service import LoginService
from server.src.common.messages.common_messages import CommonMessages
from server.src.login.services.refresh_token_service import (
    RefreshTokenService,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/login",
    summary="Login a user",
    description="Login a user with the provided details.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwic3ViIjoxfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwic3ViIjoxfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                    }
                }
            },
        },
        400: {"description": CommonMessages.BAD_REQUEST},
        401: {"description": CommonMessages.UNAUTHORIZED},
        403: {"description": CommonMessages.FORBIDDEN},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def login_user(data: UserLogin, db: Session = Depends(get_db)):
    user = LoginService.login_user(db, data)
    return user


@router.post(
    "/refresh-token",
    summary="Create a new access token",
    description="Create a new access token with the provided refresh token.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwic3ViIjoxfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                    }
                }
            },
        },
        400: {"description": CommonMessages.BAD_REQUEST},
        401: {"description": CommonMessages.UNAUTHORIZED},
        403: {"description": CommonMessages.FORBIDDEN},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def refresh_token(token: str, db: Session = Depends(get_db)):
    new_token = RefreshTokenService.refresh_token(db, token)
    return new_token


@router.post(
    "/logout",
    summary="Logout a user",
    description="Logout a user with the provided token.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": {"details": "Logged out"}
                }
            },
        },
        400: {"description": CommonMessages.BAD_REQUEST},
        401: {"description": CommonMessages.UNAUTHORIZED},
        403: {"description": CommonMessages.FORBIDDEN},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def logout(token: str, db: Session = Depends(get_db)):
    RefreshTokenService.delete_refresh_token(db, token)
    return {"details": "Logged out"}
