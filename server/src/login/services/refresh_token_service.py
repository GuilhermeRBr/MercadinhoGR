from sqlalchemy.orm import Session
from server.src.login.models.refresh_token_model import RefreshToken
from datetime import datetime, timedelta
from server.src.core.config import settings
class RefreshTokenService:
    @staticmethod
    def save_refresh_token(refresh_token, db: Session, user_id: int):

        new_refresh_token = RefreshToken(user_id=user_id, token=refresh_token, expires_at= datetime.utcnow() + timedelta(settings.REFRESH_TOKEN_EXPIRE_DAYS))

        db.add(new_refresh_token)

        db.commit()

        return refresh_token
