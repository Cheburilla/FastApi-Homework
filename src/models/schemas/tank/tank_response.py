from datetime import datetime

from pydantic import BaseModel


class TankResponse(BaseModel):
    id: int
    name: str
    max_capacity: float
    current_capacity: float
    product_id: int
    created_at: datetime
    created_by: int
    modified_at: datetime | None
    modified_by: int | None

    class Config:
        orm_mode = True
