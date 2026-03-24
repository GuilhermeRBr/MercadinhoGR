from pydantic import BaseModel, Field, ConfigDict


class UserCreate(BaseModel):
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
    confirm_password: str = Field(
        ...,
        min_length=8,
        max_length=16,
        json_schema_extra={"example": "Test@123"},
    )
    role: str = Field(
        ...,
        min_length=3,
        max_length=100,
        json_schema_extra={"example": "operator"},
    )
    active: bool = Field(..., json_schema_extra={"example": True})

    model_config = ConfigDict(from_attributes=True)


class UserActive(BaseModel):
    active: bool = Field(..., json_schema_extra={"example": True})


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


class UserResponse(BaseModel):
    id: int
    email: str
    role: str
    active: bool

    model_config = ConfigDict(from_attributes=True)
