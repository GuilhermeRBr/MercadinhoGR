from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.user.schemas.user_schema import UserCreate
from server.src.user.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/create",
    summary="Create a new user",
    description="Create a new user with the provided details.",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "Created",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "email": "email@example.com",
                        "role": "operator",
                    }
                }
            },
        },
        400: {"description": "Bad Request"},
        422: {"description": "Unprocessable Entity"},
    },
)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    new_user = UserService.create_new_user(db, data)
    return new_user


@router.get(
    "/list",
    summary="List all users",
    description="List all users.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": [
                        {"id": 1, "email": "email@example.com", "role": "operator"}
                    ]
                }
            },
        },
        404: {"description": "Not Found"},
    },
)
def list_users(db: Session = Depends(get_db)):
    user_list = UserService.get_users(db)
    return user_list
