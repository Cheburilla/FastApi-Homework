from datetime import datetime
from pydantic import BaseModel


class ProductResponse(BaseModel):
    id = int
    name = str
    created_at: datetime
    created_by: int
    modified_at: datetime | None
    modified_by: int | None

    class Config:
        orm_mode = True
