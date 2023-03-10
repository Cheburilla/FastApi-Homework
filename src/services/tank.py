from datetime import datetime
from typing import List

from fastapi import Depends

from db.db import Session, get_session
from services.user import get_current_user_id
from src.models.schemas.tank.tank_request import TankRequest
from src.models.tank import Tank


class TankService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def all(self) -> List[Tank]:
        tanks = (
            self.session
            .query(Tank)
            .order_by(
                Tank.id.desc()
            )
            .all()
        )
        return tanks

    def get(self, tank_id: int) -> Tank:
        tank = (
            self.session
            .query(Tank)
            .filter(
                Tank.id == tank_id
            )
            .first()
        )
        return tank

    def add(self, tank_schema: TankRequest, creating_id: int) -> Tank:
        tank = Tank(**tank_schema.dict())
        tank.created_at = datetime.now()
        tank.created_by = creating_id
        self.session.add(tank)
        self.session.commit()
        return tank

    def update(self, tank_id: int, tank_schema: TankRequest, modifying_id: int) -> Tank:
        tank = self.get(tank_id)
        for field, value in tank_schema:
            setattr(tank, field, value)
        tank.modified_at = datetime.now()
        tank.modified_by = modifying_id
        self.session.commit()
        return tank

    def delete(self, tank_id: int):
        tank = self.get(tank_id)
        self.session.delete(tank)
        self.session.commit()

    def update_current_capacity(self, tank_id: int, new_capacity: float, modifying_id: int) -> Tank:
        tank = self.get(tank_id)
        tank.current_capacity = new_capacity
        tank.modified_by = modifying_id
        tank.modified_at = datetime.now()
        self.session.commit()
        return tank
