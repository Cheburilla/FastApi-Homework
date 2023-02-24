from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.schemas.user.user_request import UserRequest
from services.user import UserService, get_current_user_id

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/all', response_model=List[UserResponse], name='Получить все категории')
def get(user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id)):
    """
    Получить все категории. Более подробное описание.
    """
    print(user_id)
    return user_service.all()


@router.get('/get/{user_id}', response_model=UserResponse, name='Получить одну категорию')
def get(user_id: int, user_service: UserService = Depends()):
    return get_with_check(user_id, user_service)


def get_with_check(user_id: int, user_service: UserService):
    result = user_service.get(user_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Категория не найдена")
    return result


@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED, name='Добавить категорию')
def add(user_schema: UserRequest, user_service: UserService = Depends()):
    return user_service.add(user_schema)


@router.put('/{user_id}', response_model=UserResponse, name='Обновить информацию о категории')
def put(user_id: int, user_schema: UserRequest, user_service: UserService = Depends()):
    get_with_check(user_id, user_service)
    return user_service.add(user_schema)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, name='Удалить категорию')
def delete(user_id: int, user_service: UserService = Depends()):
    get_with_check(user_id, user_service)
    return user_service.delete(user_id)


@router.post('/register', status_code=status.HTTP_201_CREATED, name='Регистрация')
def register(user_schema: UserRequest, users_service: UsersService = Depends()):
    return users_service.register(user_schema)


@router.post('/authorize', response_model=JwtToken, name='Авторизация')
def authorize(auth_schema: OAuth2PasswordRequestForm = Depends(), users_service: UsersService = Depends()):
    result = users_service.authorize(
        auth_schema.username, auth_schema.password)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Не авторизован')
    return result
