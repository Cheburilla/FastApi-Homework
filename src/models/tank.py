from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import Base


class Tank(Base):
    __tablename__ = 'Tanks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    max_capacity = Column(Float)
    current_capacity = Column(Float)
    product_id = Column(Integer, ForeignKey(
        'Products.id'), index=True)  # id продукта
    created_at = Column(DateTime)
    # id пользователя, который добавил объект
    created_by = Column(Integer, ForeignKey(
        'Users.id'), index=True)
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, ForeignKey(
        'Users.id'), index=True, nullable=True)
