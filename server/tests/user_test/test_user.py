from server.src.user.schemas.user_schema import UserCreate
from server.src.user.services.user_service import UserService


def test_create_user_success(db):
    data = UserCreate(
        email="email@example.com",
        password="Test@123",
        confirm_password="Test@123",
        role="operator",
        active=True,
    )

    user = UserService.create_new_user(db, data)

    assert user.email == data.email
