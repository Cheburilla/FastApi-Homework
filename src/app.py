from fastapi import FastAPI

from src.api.base_router import router

app = FastAPI(
    title='Мое второе приложение FastAPI',
    description='Приложение для работы с резервуарами',
    version='alpha'
)

app.include_router(router)
