from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.schemas.operation.operation_request import OperationRequest
from src.models.base import Base


class Operation(Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    mass = Column(Float)
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    tank_id = Column(Integer, ForeignKey('tanks.id'), index=True)
    product_id = Column(Integer, ForeignKey(
        'products.id'), index=True)  # id продукта
    created_at = Column(DateTime)
    # id пользователя, который добавил объект
    created_by = Column(Integer, ForeignKey('users.id'), index=True)
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, ForeignKey(
        'users.id'), index=True, nullable=True)
    created = relationship('User', backref='users')
    modified = relationship('User', backref='users')
    product = relationship('Product', backref='products')
    tank = relationship('Tank', backref='tanks')
