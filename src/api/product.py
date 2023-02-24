from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.schemas.product.product_request import ProductRequest
from models.schemas.product.product_response import ProductResponse
from services.product import ProductService
from services.user import get_current_user_id

router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.get('/all', response_model=List[ProductResponse], name='Получить все категории')
def get(product_service: ProductService = Depends(), user_id: int = Depends(get_current_user_id)):
    """
    Получить все категории. Более подробное описание.
    """
    print(user_id)
    return product_service.all()


@router.get('/get/{product_id}', response_model=ProductResponse, name='Получить одну категорию')
def get(product_id: int, product_service: ProductService = Depends()):
    return get_with_check(product_id, product_service)


def get_with_check(product_id: int, product_service: ProductService):
    result = product_service.get(product_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Категория не найдена")
    return result


@router.post('/', response_model=ProductResponse, status_code=status.HTTP_201_CREATED, name='Добавить категорию')
def add(product_schema: ProductRequest, product_service: ProductService = Depends()):
    return product_service.add(product_schema)


@router.put('/{product_id}', response_model=ProductResponse, name='Обновить информацию о категории')
def put(product_id: int, product_schema: ProductRequest, product_service: ProductService = Depends()):
    get_with_check(product_id, product_service)
    return product_service.add(product_schema)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT, name='Удалить категорию')
def delete(product_id: int, product_service: ProductService = Depends()):
    get_with_check(product_id, product_service)
    return product_service.delete(product_id)
