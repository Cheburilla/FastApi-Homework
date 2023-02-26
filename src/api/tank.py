from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.schemas.tank.tank_request import TankRequest
from models.schemas.tank.tank_response import TankResponse
from services.tank import TankService
from services.user import get_current_user_id
from src.api.utils.get_with_check import get_with_check

router = APIRouter(
    prefix='/tanks',
    tags=['tanks']
)


@router.get('/all', response_model=List[TankResponse], name='Получить все резервуары')
def get(tank_service: TankService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
    return tank_service.all()


@router.get('/get/{tank_id}', response_model=TankResponse, name='Получить один резервуар')
def get(tank_id: int, tank_service: TankService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
    return get_with_check(tank_id, tank_service)


@router.post('/', response_model=TankResponse, status_code=status.HTTP_201_CREATED, name='Добавить резервуар')
def add(tank_schema: TankRequest, tank_service: TankService = Depends(), creating_id: int = Depends(get_current_user_id)):
    print(creating_id)
    return tank_service.add(tank_schema, creating_id)


@router.put('/{tank_id}', response_model=TankResponse, name='Обновить информацию о резервуаре')
def put(tank_id: int, tank_schema: TankRequest, tank_service: TankService = Depends(), modifying_id: int = Depends(get_current_user_id)):
    get_with_check(tank_id, tank_service)
    return tank_service.add(tank_schema, modifying_id)


@router.delete('/{tank_id}', status_code=status.HTTP_204_NO_CONTENT, name='Удалить резервуар')
def delete(tank_id: int, tank_service: TankService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
    get_with_check(tank_id, tank_service)
    return tank_service.delete(tank_id)


@router.get('/update_current_capacity/{tank_id}', response_model=TankResponse, name='Изменение значения current_capacity')
def change(tank_id: int, new_capacuty: float, tanks_service: TankService = Depends(), modifying_id: int = Depends(get_current_user_id)):
    """
    Обновление информации о поле current_capacity (с проверкой на наличие записи в БД)
    """
    get_with_check(tank_id, tanks_service)
    return tanks_service.update_current_capacity(tank_id, new_capacuty, modifying_id)
