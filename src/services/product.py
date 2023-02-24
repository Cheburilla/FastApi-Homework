from datetime import datetime
from typing import List

from fastapi import Depends

from db.db import Session, get_session
from services.user import get_current_user_id
from src.models.product import Product
from src.models.schemas.product.product_request import ProductRequest


class ProductService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def all(self) -> List[Product]:
        products = (
            self.session
            .query(Product)
            .order_by(
                Product.id.desc()
            )
            .all()
        )
        return products

    def get(self, product_id: int) -> Product:
        product = (
            self.session
            .query(Product)
            .filter(
                Product.id == product_id
            )
            .first()
        )
        return product

    def add(self, product_schema: ProductRequest) -> Product:
        product = Product(**product_schema.dict())
        product.created_at = datetime.now()
        product.created_by = get_current_user_id()
        self.session.add(product)
        self.session.commit()
        return product

    def update(self, product_id: int, product_schema: ProductRequest) -> Product:
        product = self.get(product_id)
        for field, value in product_schema:
            setattr(product, field, value)
        product.modified_at = datetime.now()
        product.modified_by = get_current_user_id()
        self.session.commit()
        return product

    def delete(self, product_id: int):
        product = self.get(product_id)
        self.session.delete(product)
        self.session.commit()
