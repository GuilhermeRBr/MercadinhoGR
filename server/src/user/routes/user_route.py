from fastapi import APIRouter, Depends, status, Path
from sqlalchemy.orm import Session
from server.src.core.dependency import get_current_user
from server.src.data.database import get_db
from server.src.user.schemas.user_schema import (
    UserCreate,
    UserActive,
)
from server.src.user.services.user_service import UserService
from server.src.common.messages.common_messages import CommonMessages

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/register",
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
                        "active": True,
                    }
                }
            },
        },
        400: {"description": CommonMessages.BAD_REQUEST},
        401: {"description": CommonMessages.UNAUTHORIZED},
        409: {"description": CommonMessages.CONFLICT},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def create_user(
    data: UserCreate,
    user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    new_user = UserService.create_new_user(db, data, user)
    return new_user


@router.get(
    "/",
    summary="List all users",
    description="List all users.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "email": "email@example.com",
                            "role": "operator",
                            "active": True,
                        },
                    ]
                }
            },
        },
        400: {"description": CommonMessages.BAD_REQUEST},
        401: {"description": CommonMessages.UNAUTHORIZED},
        404: {"description": CommonMessages.NOT_FOUND},
    },
)
def list_users(
    _: str = Depends(get_current_user), db: Session = Depends(get_db)
):
    user_list = UserService.get_users(db)
    return user_list


@router.get(
    "/{id}",
    summary="Get a user by ID",
    description="Retrieve a user by its unique ID",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "email": "email@example.com",
                        "role": "operator",
                        "active": True,
                    }
                }
            },
        },
        400: {"description": CommonMessages.BAD_REQUEST},
        401: {"description": CommonMessages.UNAUTHORIZED},
        404: {"description": CommonMessages.NOT_FOUND},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def get_by_id(
    id: int = Path(..., ge=1, le=2_147_483_647),
    _: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = UserService.get_user_by_id(db, id)
    return user


@router.patch(
    "/{id}",
    summary="Update a user",
    description="Update an existing user with new details.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "email": "email@example.com",
                        "role": "operator",
                        "active": True,
                    }
                }
            },
        },
        400: {"description": CommonMessages.BAD_REQUEST},
        401: {"description": CommonMessages.UNAUTHORIZED},
        404: {"description": CommonMessages.NOT_FOUND},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def patch_user(
    id: int = Path(..., ge=1, le=2_147_483_647),
    data: UserActive = ...,
    _: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    updated_user = UserService.activate_user(db, id, data)
    return updated_user
