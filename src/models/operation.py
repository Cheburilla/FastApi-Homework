from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.schemas.operation.operation_request import OperationRequest
from models.user import User
from src.models.base import Base


class Operation(Base):
    __tablename__ = 'Operations'
    id = Column(Integer, primary_key=True)
    mass = Column(Float)
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    tank_id = Column(Integer, ForeignKey('Tanks.id'), index=True)
    product_id = Column(Integer, ForeignKey(
        'Products.id'), index=True)
    created_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey(
        'Users.id'), index=True)
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, ForeignKey(
        'Users.id'), index=True, nullable=True)

    tank = relationship('Tanks', foreign_keys=[tank_id], backref='tanks')
    product1 = relationship('Products', foreign_keys=[
                            product_id], backref='products1')
    created11 = relationship('Users', foreign_keys=[
                             created_by], backref='users1.1')
    modified12 = relationship('Users', foreign_keys=[
                              modified_by], backref='users1.2')
