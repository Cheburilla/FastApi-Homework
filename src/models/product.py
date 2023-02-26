from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import Base


class Product(Base):
    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey(
        'Users.id'), index=True)
    modified_at = Column(DateTime, nullable=True)
    modified_by = Column(Integer, ForeignKey(
        'Users.id'), index=True, nullable=True)

    created21 = relationship('src.models.user.User', foreign_keys=[
                             created_by], backref='users2.1')
    modified22 = relationship('src.models.user.User', foreign_keys=[
                              modified_by], backref='users2.2')
