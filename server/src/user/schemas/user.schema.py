class UserCreate:
    email: str
    password: str
    role: str

    class Config:
        from_attributes = True


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True
