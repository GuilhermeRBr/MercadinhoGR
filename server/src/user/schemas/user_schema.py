from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    email: str = Field(..., min_length=3, max_length=100, example="email@dominio.com")
    password: str = Field(..., min_length=8, max_length=16, example="Test@123")
    confirm_password: str = Field(..., min_length=8, max_length=16, example="Test@123")
    role: str = Field(..., min_length=3, max_length=100, example="operator")
    active: bool = Field(..., example=True)

    class Config:
        from_attributes = True


class UserActive(BaseModel):
    active: bool = Field(..., example=True)


class UserResponse(BaseModel):
    id: int
    email: str
    role: str
    active: bool

    class Config:
        from_attributes = True
