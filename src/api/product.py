from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.schemas.product.product_request import ProductRequest
from models.schemas.product.product_response import ProductResponse
from services.product import ProductService
from services.user import get_current_user_id
from src.api.utils.get_with_check import get_with_check

router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.get('/all', response_model=List[ProductResponse], name='Получить все продукты')
def get(product_service: ProductService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
    return product_service.all()


@router.get('/get/{product_id}', response_model=ProductResponse, name='Получить один продукт')
def get(product_id: int, product_service: ProductService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
    return get_with_check(product_id, product_service)


@router.post('/', response_model=ProductResponse, status_code=status.HTTP_201_CREATED, name='Добавить продукты')
def add(product_schema: ProductRequest, product_service: ProductService = Depends(), creating_id: int = Depends(get_current_user_id)):
    print(creating_id)
    return product_service.add(product_schema, creating_id)


@router.put('/{product_id}', response_model=ProductResponse, name='Обновить информацию о продукте')
def put(product_id: int, product_schema: ProductRequest, product_service: ProductService = Depends(), modifying_id: int = Depends(get_current_user_id)):
    get_with_check(product_id, product_service)
    return product_service.add(product_schema, modifying_id)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT, name='Удалить продукт')
def delete(product_id: int, product_service: ProductService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
    get_with_check(product_id, product_service)
    return product_service.delete(product_id)
