from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.schemas.tank.tank_request import TankRequest
from models.schemas.tank.tank_response import TankResponse
from services.tank import TankService
from services.user import get_current_user_id

router = APIRouter(
    prefix='/tanks',
    tags=['tanks']
)


@router.get('/all', response_model=List[TankResponse], name='Получить все категории')
def get(tank_service: TankService = Depends(), user_id: int = Depends(get_current_user_id)):
    """
    Получить все категории. Более подробное описание.
    """
    print(user_id)
    return tank_service.all()


@router.get('/get/{tank_id}', response_model=TankResponse, name='Получить одну категорию')
def get(tank_id: int, tank_service: TankService = Depends()):
    return get_with_check(tank_id, tank_service)


def get_with_check(tank_id: int, tank_service: TankService):
    result = tank_service.get(tank_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Категория не найдена")
    return result


@router.post('/', response_model=TankResponse, status_code=status.HTTP_201_CREATED, name='Добавить категорию')
def add(tank_schema: TankRequest, tank_service: TankService = Depends()):
    return tank_service.add(tank_schema)


@router.put('/{tank_id}', response_model=TankResponse, name='Обновить информацию о категории')
def put(tank_id: int, tank_schema: TankRequest, tank_service: TankService = Depends()):
    get_with_check(tank_id, tank_service)
    return tank_service.add(tank_schema)


@router.delete('/{tank_id}', status_code=status.HTTP_204_NO_CONTENT, name='Удалить категорию')
def delete(tank_id: int, tank_service: TankService = Depends()):
    get_with_check(tank_id, tank_service)
    return tank_service.delete(tank_id)
