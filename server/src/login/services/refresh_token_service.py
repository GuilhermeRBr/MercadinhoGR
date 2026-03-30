from sqlalchemy.orm import Session
from server.src.login.models.refresh_token_model import RefreshToken
from datetime import datetime, timedelta
from fastapi import HTTPException
from server.src.core.config import settings
from server.src.core.security import create_access_token


class RefreshTokenService:
    @staticmethod
    def save_refresh_token(refresh_token, db: Session, user_id: int):

        new_refresh_token = RefreshToken(
            user_id=user_id,
            token=refresh_token,
            expires_at=datetime.utcnow()
            + timedelta(settings.REFRESH_TOKEN_EXPIRE_DAYS),
        )

        db.add(new_refresh_token)

        db.commit()

        return refresh_token

    @staticmethod
    def refresh_token(db: Session, token: str):
        refresh_token = (
            db.query(RefreshToken)
            .filter(RefreshToken.token == token)
            .first()
        )
        if not refresh_token:
            raise HTTPException(
                status_code=401, detail="Invalid refresh token"
            )

        if refresh_token.expires_at < str(datetime.utcnow()):
            raise HTTPException(
                status_code=401, detail="Refresh token expired"
            )

        new_access_token = create_access_token(
            data={"sub": refresh_token.user_id}
        )

        return {"access_token": new_access_token}

    @staticmethod
    def delete_refresh_token(db: Session, token: str):
        refresh_token = (
            db.query(RefreshToken)
            .filter(RefreshToken.token == token)
            .first()
        )
        if not refresh_token:
            raise HTTPException(
                status_code=401, detail="Invalid refresh token"
            )
        db.delete(refresh_token)
        db.commit()
