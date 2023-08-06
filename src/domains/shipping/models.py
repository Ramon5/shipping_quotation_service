from sqlalchemy import Column
from sqlalchemy.types import Float, Integer, String

from src.infra.database.base import ITable


class Shipping(ITable):
    name = Column(String, nullable=False)
    shipping_rate = Column(Float, nullable=False)
    minimum_height = Column(Integer, nullable=False)
    maximum_height = Column(Integer, nullable=False)
    minimum_width = Column(Integer, nullable=False)
    maximum_width = Column(Integer, nullable=False)
    shipping_deadline = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"
