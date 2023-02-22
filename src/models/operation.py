from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from src.models.base import Base
from sqlalchemy.orm import relationship

class Operation(Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    mass = Column(Float)
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    tank_id = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'), index=True) # id продукта
    created_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey('users.id'), index=True) # id пользователя, который добавил объект
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, ForeignKey('users.id'), index=True, nullable=True)
    product = relationship('Product', backref='products')
    created = relationship('User', backref='users')
    modified = relationship('User', backref='users')
    
    