from typing import Optional
from app.models.user_models import UserInDB
from passlib.context import CryptContext

class UserService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    users_db = {}  # Simulate a user database

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def get_user(cls, username: str) -> Optional[UserInDB]:
        if username in cls.users_db:
            user_dict = cls.users_db[username]
            return UserInDB(**user_dict)
        return None

    @classmethod
    def authenticate_user(cls, username: str, password: str) -> Optional[UserInDB]:
        user = cls.get_user(username)
        if not user or not cls.verify_password(password, user.hashed_password):
            return None
        return user
