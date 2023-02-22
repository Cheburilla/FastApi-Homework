from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from src.models.base import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey('users.id'), index=True) # id пользователя, который добавил объект
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, ForeignKey('users.id'), index=True, nullable=True)
    created = relationship('User', backref='users')
    modified = relationship('User', backref='users')
    