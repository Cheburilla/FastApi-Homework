import csv
from datetime import datetime
from io import StringIO
from typing import List

from fastapi import Depends

from db.db import Session, get_session
from models.operation import Operation
from models.schemas.operation.operation_request import OperationRequest
from services.user import get_current_user_id


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

    def add(self, operation_schema: OperationRequest, creating_id: int) -> Operation:
        operation = Operation(**operation_schema.dict())
        operation.created_at = datetime.now()
        operation.created_by = creating_id
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, operation_id: int, operation_schema: OperationRequest, modifying_id: int) -> Operation:
        operation = self.get(operation_id)
        for field, value in operation_schema:
            setattr(operation, field, value)
        operation.modified_at = datetime.now()
        operation.modified_by = modifying_id
        self.session.commit()
        return operation

    def delete(self, operation_id: int):
        operation = self.get(operation_id)
        self.session.delete(operation)
        self.session.commit()

    def download(self, tank_id: int, product_id: int, date_start: datetime, date_end: datetime):
        operations = (
            self.session
                .query(Operation)
            .filter(Operation.tank_id == tank_id,
                    Operation.product_id == product_id,
                    Operation.date_start >= date_start,
                    Operation.date_end <= date_end
                    )
            .order_by(Operation.id.asc())
            .all()
        )

        columns_name = Operation.__table__.columns.keys()

        list = [dict([(key, row.__dict__[key]) for key in columns_name])
                for row in operations]

        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=columns_name)
        writer.writeheader()

        for row in list:
            writer.writerow(row)
        output.seek(0)

        return output
