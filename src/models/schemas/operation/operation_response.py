from datetime import datetime

from pydantic import BaseModel


class OperationResponse(BaseModel):
    id: int
    mass: float
    date_start: datetime
    date_end: datetime
    tank_id: int
    product_id: int
    created_at: datetime
    created_by: int
    modified_at: datetime | None
    modified_by: int | None

    class Config:
        orm_mode = True
