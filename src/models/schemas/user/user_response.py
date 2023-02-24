from datetime import datetime

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    username: str
    password_hash: str
    role: str
    current_capacity: float
    created_at: datetime
    created_by: int
    modified_at: datetime
    modified_by: int

    class Config:
        orm_mode = True
