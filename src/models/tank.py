from sqlalchemy import Column, Integer, String, DateTime, Float
from src.models.base import Base


class Tank(Base):
    __tablename__ = 'tanks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    max_capacity = Column(Float)
    current_capacity = Column(Float)
    product_id = Column(Integer) # id продукта
    created_at = Column(DateTime)
    created_by = Column(Integer) # id пользователя, который добавил объект
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, nullable=True)
    