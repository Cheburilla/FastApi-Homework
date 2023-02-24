from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.schemas.operation.operation_request import OperationRequest
from models.schemas.operation.operation_response import OperationResponse
from services.operation import OperationService
from services.user import get_current_user_id

router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/all', response_model=List[OperationResponse], name='Получить все операции')
def get(operations_service: OperationService = Depends(), user_id: int = Depends(get_current_user_id)):
    """
    Получить все операции. Более подробное описание.
    """
    print(user_id)
    return operations_service.all()


@router.get('/get/{operation_id}', response_model=OperationResponse, name='Получить одну операцию')
def get(operation_id: int, operations_service: OperationService = Depends(), user_id: int = Depends(get_current_user_id)):
    return get_with_check(operation_id, operations_service)


def get_with_check(operation_id: int, operations_service: OperationService):
    result = operations_service.get(operation_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Операция не найдена")
    return result


@router.post('/', response_model=OperationResponse, status_code=status.HTTP_201_CREATED, name='Добавить операцию')
def add(operation_schema: OperationRequest, operations_service: OperationService = Depends(), user_id: int = Depends(get_current_user_id)):
    return operations_service.add(operation_schema)


@router.put('/{operation_id}', response_model=OperationResponse, name='Обновить информацию о операции')
def put(operation_id: int, operation_schema: OperationRequest, operations_service: OperationService = Depends(), user_id: int = Depends(get_current_user_id)):
    get_with_check(operation_id, operations_service)
    return operations_service.add(operation_schema)


@router.delete('/{operation_id}', status_code=status.HTTP_204_NO_CONTENT, name='Удалить операцию')
def delete(operation_id: int, operations_service: OperationService = Depends(), user_id: int = Depends(get_current_user_id)):
    get_with_check(operation_id, operations_service)
    return operations_service.delete(operation_id)
