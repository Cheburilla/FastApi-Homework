from fastapi import FastAPI

from core import settings
from db.db import Session
from models.user import User
from services.user import UserService
from src.api.base_router import router

tags_dict = [
    {
        'name': 'operations',
        'description': 'Информация об операциях с резервуарами'
    },
    {
        'name': 'users',
        'description': 'Информация об операциях с пользователями и регистрация'
    },
    {
        'name': 'tanks',
        'description': 'Информация о резервуарах'
    },
    {
        'name': 'products',
        'description': 'Информация о продуктах'
    },
    {
        'name': 'authorization',
        'description': 'Авторизация и регистрация пользователей'
    },
]


def admin_check() -> None:
    with Session.begin() as session:
        user = (
            session
            .query(User)
            .filter(User.role == 'admin')
            .first()
        )
        if not user:
            admin = User(
                id=1,
                username=settings.admin_login,
                password_hashed=UserService.hash_password(
                    settings.admin_password),
                role='admin'
            )
            session.add(admin)
            session.commit()


app = FastAPI(
    title='Мое второе приложение FastAPI',
    description='Приложение для работы с резервуарами',
    version='alpha',
    openapi_tags=tags_dict,
    on_startup=[admin_check]
)

app.include_router(router)
