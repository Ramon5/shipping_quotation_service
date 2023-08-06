from typing import Optional

from pydantic import BaseModel, conint


class DimenssionDTO(BaseModel):
    height: int
    width: int


class ShippingRequestDTO(BaseModel):
    dimension: DimenssionDTO
    weight: conint(gt=0)


class ShippingOutputDTO(BaseModel):
    name: str
    value: float
    shipping_deadline: int

class ShippingInputDTO(BaseModel):
    name: str
    shipping_rate: float
    minimum_height: int
    maximum_height: int
    minimum_width: int
    maximum_width: int
    shipping_deadline: int
