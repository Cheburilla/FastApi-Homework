from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException
from jose import JWTError
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.schemas.utils.jwt_token import JwtToken
from src.core.settings import settings
from src.models.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hashed = Column(String)
    role = Column(String)
    created_at = Column(DateTime)  # id пользователя, который добавил объект
    created_by = Column(Integer, ForeignKey('users.id'), index=True)
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, ForeignKey(
        'users.id'), index=True, nullable=True)
    created = relationship('User', backref='users')
    modified = relationship('User', backref='users')
