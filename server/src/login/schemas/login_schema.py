from pydantic import BaseModel, Field, ConfigDict


class UserLogin(BaseModel):
    email: str = Field(
        ...,
        min_length=3,
        max_length=100,
        json_schema_extra={"example": "email@dominio.com"},
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=16,
        json_schema_extra={"example": "Test@123"},
    )

    model_config = ConfigDict(from_attributes=True)


class LoginResponse(BaseModel):
    access_token: str
