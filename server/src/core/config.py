from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")
    SECRET_KEY: str
    DATABASE_URL: str
    DEBUG: bool = False


settings = Settings()
