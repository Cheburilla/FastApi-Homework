from typing import List
from fastapi import Depends

from db.db import Session, get_session
from models.operation import Operation


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
        
    def all(self) -> List[Operation]:
        operations = (
            self.session
            .query(Operation)
            .order_by(
                Operation.id.desc()
            )
            .all()
        )
        return operations
    
    def get(self, operation_id: int) -> Operation:
        operation = (
            self.session
            .query(Operation)
            .filter(
                Operation.id == operation_id
            )
            .first()
        )
        return operation
    
    