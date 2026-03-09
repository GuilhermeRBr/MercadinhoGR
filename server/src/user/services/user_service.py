from sqlalchemy.orm import Session
from server.src.user.models.user_model import User
from server.src.user.schemas.user_schema import UserCreate, UserResponse
from fastapi import HTTPException, status
import bcrypt


class UserService:
    @staticmethod
    def create_new_user(db: Session, data: UserCreate):

        if db.query(User).filter(User.email == data.email).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe um usuário cadastrado com esse email",
            )
        if db.query(User).filter(User.role == "owner").first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe um proprietário cadastrado",
            )

        if data.password != data.confirm_password:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="As senhas devem ser iguais",
            )

        password_hash = bcrypt.hashpw(
            data.password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
        new_user = User(email=data.email, password=password_hash, role=data.role)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return UserResponse.model_validate(new_user)
