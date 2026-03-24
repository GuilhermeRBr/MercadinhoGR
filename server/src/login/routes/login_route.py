from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.login.schemas.login_schema import UserLogin
from server.src.login.services.login_service import LoginService
from server.src.common.messages.common_messages import CommonMessages

router = APIRouter(prefix="/login", tags=["Login"])


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
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def login_user(data: UserLogin, db: Session = Depends(get_db)):
    user = LoginService.login_user(db, data)
    return user
