from datetime import datetime, timedelta
from typing import Optional, Dict
from jose import jwt
from app.core.auth import SECRET_KEY, ALGORITHM

class TokenService:
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_token(token: str) -> Dict:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
