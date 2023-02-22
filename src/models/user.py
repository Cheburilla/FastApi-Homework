from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException
from jose import JWTError
from sqlalchemy import Column, Integer, String, DateTime, Float
from models.schemas.utils.jwt_token import JwtToken
from src.models.base import Base
from src.core.settings import settings


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hashed = Column(String)
    role = Column(String)
    created_at = Column(DateTime)
    created_by = Column(Integer) # id пользователя, который добавил объект
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, nullable=True)
