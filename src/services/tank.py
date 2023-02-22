from datetime import datetime
from typing import List
from fastapi import Depends

from db.db import Session, get_session
from src.models.tank import Tank
from src.models.schemas.tank.tank_request import TankRequest


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
    
    def add(self, tank_schema: TankRequest) -> Tank:
        tank = tank(**tank_schema.dict())
        tank.created_at = datetime.now()
        #tank.created_by = 
        self.session.add(tank)
        self.session.commit()
        return tank
    
    def update(self, tank_id: int, tank_schema: TankRequest) -> Tank:
        tank = self.get(tank_id)
        for field, value in tank_schema:
            setattr(tank, field, value)
        tank.modified_at = datetime.now()
        #tank.modified_by = 
        self.session.commit()
        return tank
    
    def delete(self, tank_id: int):
        tank = self.get(tank_id)
        self.session.delete(tank)
        self.session.commit()
