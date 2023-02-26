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
        'Products.id'), index=True)
    created_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey(
        'Users.id'), index=True)
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, ForeignKey(
        'Users.id'), index=True, nullable=True)

    product2 = relationship('Product', backref='products2')
    created31 = relationship('src.models.user.User', foreign_keys=[
                             created_by], backref='users3.1')
    modified32 = relationship('src.models.user.User', foreign_keys=[
                              modified_by], backref='users3.2')
