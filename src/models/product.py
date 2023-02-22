from sqlalchemy import Column, Integer, String, DateTime, Float
from src.models.base import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime)
    created_by = Column(Integer) # id пользователя, который добавил объект
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, nullable=True)
    