from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.user.schemas.user_schema import UserCreate
from server.src.user.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    new_user = UserService.create_new_user(db, data)
    return new_user
    return new_user
