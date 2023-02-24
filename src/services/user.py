from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import pbkdf2_sha256

from core.settings import settings
from src.db.db import Session, get_session
from src.models.schemas.user.user_request import UserRequest
from src.models.schemas.utils.jwt_token import JwtToken
from src.models.user import User

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/users/authorize')


def get_current_user_id(token: str = Depends(oauth2_schema)) -> int:
    return UserService.verify_token(token)


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    @staticmethod
    def hash_password(password: str) -> str:
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def check_password(password_text: str, password_hash: str) -> bool:
        return pbkdf2_sha256.verify(password_text, password_hash)

    @staticmethod
    def create_token(user_id: int) -> JwtToken:
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'exp': now + timedelta(seconds=settings.jwt_expires_seconds),
            'sub': str(user_id),
        }
        token = jwt.encode(payload, settings.jwt_secret,
                           algorithm=settings.jwt_algorithm)
        return JwtToken(access_token=token)

    @staticmethod
    def verify_token(token: str) -> Optional[int]:
        try:
            payload = jwt.decode(token, settings.jwt_secret, algorithms=[
                                 settings.jwt_algorithm])
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Некорректный токен")

        return payload.get('sub')

    def register(self, user_schema: UserRequest) -> None:
        user = User(
            username=user_schema.username,
            password_hash=self.hash_password(user_schema.password_text),
        )
        self.session.add(user)
        self.session.commit()

    def authorize(self, username: str, password_text: str) -> Optional[JwtToken]:
        user = (
            self.session
            .query(User)
            .filter(User.username == username)
            .first()
        )

        if not user:
            return None
        if not self.check_password(password_text, user.password_hash):
            return None

        return self.create_token(user.id)
