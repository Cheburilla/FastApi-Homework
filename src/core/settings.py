from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = 'localhost'
    port: int = 9999
    
    
settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8'
)
