from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse

from models.schemas.operation.operation_request import OperationRequest
from models.schemas.operation.operation_response import OperationResponse
from services.operation import OperationService
from services.tank import TankService
from services.user import get_current_user_id
from src.api.utils.get_with_check import get_with_check

router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/all', response_model=List[OperationResponse], name='Получить все операции')
def get(operations_service: OperationService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
    return operations_service.all()


@router.get('/get/{operation_id}', response_model=OperationResponse, name='Получить одну операцию')
def get(operation_id: int, operations_service: OperationService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
    return get_with_check(operation_id, operations_service)


@router.post('/', response_model=OperationResponse, status_code=status.HTTP_201_CREATED, name='Добавить операцию')
def add(operation_schema: OperationRequest, operations_service: OperationService = Depends(), creating_id: int = Depends(get_current_user_id)):
    print(creating_id)
    return operations_service.add(operation_schema, creating_id)


@router.put('/{operation_id}', response_model=OperationResponse, name='Обновить информацию о операции')
def put(operation_id: int, operation_schema: OperationRequest, operations_service: OperationService = Depends(), modifying_id: int = Depends(get_current_user_id)):
    get_with_check(operation_id, operations_service)
    print(modifying_id)
    return operations_service.add(operation_schema, modifying_id)


@router.delete('/{operation_id}', status_code=status.HTTP_204_NO_CONTENT, name='Удалить операцию')
def delete(operation_id: int, operations_service: OperationService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
    get_with_check(operation_id, operations_service)
    return operations_service.delete(operation_id)


@router.get('/get_by_tank_id/{tank_id}', response_model=list[OperationResponse], name='Получить все операции по конкретному резервуару')
def get_by_tank(tank_id: int, operations_service: OperationService = Depends(), tank_service: TankService = Depends()):
    get_with_check(tank_id, tank_service)
    return operations_service.find_by_tank(tank_id)


@router.get('/download', response_model=List[OperationResponse], name='Формирование отчета')
def report(tank_id: int, product_id: int, date_start: datetime, date_end: datetime, operations_service: OperationService = Depends()):
    """
    Формирование отчета в формате csv
    """
    report = operations_service.download(
        tank_id, product_id, date_start, date_end)
    return StreamingResponse(report, media_type='text/csv',
                             headers={
                                 'Content-Disposition': 'attachment; filename=report.csv'
                             })
