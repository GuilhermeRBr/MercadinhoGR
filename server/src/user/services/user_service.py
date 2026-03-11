from sqlalchemy.orm import Session
from server.src.user.models.user_model import User
from server.src.user.schemas.user_schema import UserCreate, UserResponse
from fastapi import HTTPException
import bcrypt
from server.src.user.messages.user_message import USER_MESSAGES


class UserService:
    @staticmethod
    def create_new_user(db: Session, data: UserCreate):

        if db.query(User).filter(User.email == data.email).first():
            raise HTTPException(
                status_code=409,
                detail=USER_MESSAGES.EMAIL_ALREADY_EXISTS,
            )
        if db.query(User).filter(User.role == "owner").first():
            raise HTTPException(
                status_code=409, detail=USER_MESSAGES.USER_ALREADY_EXISTS
            )

        if data.password != data.confirm_password:
            raise HTTPException(
                status_code=422,
                detail=USER_MESSAGES.PASSWORDS_NOT_MATCH,
            )

        password_hash = bcrypt.hashpw(
            data.password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
        new_user = User(email=data.email, password=password_hash, role=data.role)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return UserResponse.model_validate(new_user)

    @staticmethod
    def get_users(db: Session):
        users = db.query(User).all()

        if not users:
            raise HTTPException(
                status_code=404,
                detail=USER_MESSAGES.NO_USERS_FOUND,
            )

        return [UserResponse.model_validate(user) for user in users]

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail=USER_MESSAGES.USER_NOT_FOUND,
            )

        return UserResponse.model_validate(user)
