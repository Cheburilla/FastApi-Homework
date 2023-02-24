from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime)
    # id пользователя, который добавил объект
    created_by = Column(Integer, ForeignKey('users.id'), index=True)
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, ForeignKey(
        'users.id'), index=True, nullable=True)
    created = relationship('User', backref='users')
    modified = relationship('User', backref='users')
