from typing import List, Optional

from src.domains.shipping.dtos import (
    ShippingInputDTO,
    ShippingOutputDTO,
    ShippingRequestDTO,
)
from src.domains.shipping.models import Shipping
from src.infra.database.repository.repository import IRepository


class ShippingController:
    def __init__(self, repository: IRepository) -> None:
        self.repository = repository

    def _calculate_shipping_price(
        self, shipping_object: Shipping, weight: int
    ) -> ShippingOutputDTO:
        price = (weight * shipping_object.shipping_rate) / 10
        return price

    async def get_shipping_quotation(
        self, shipping_request: ShippingRequestDTO
    ) -> List[Optional[ShippingOutputDTO]]:
        if shipping_objects := await self.repository.query_shipping(shipping_request):
            return [
                ShippingOutputDTO(
                    name=shipping_object.name,
                    value=self._calculate_shipping_price(
                        shipping_object, shipping_request.weight
                    ),
                    shipping_deadline=shipping_object.shipping_deadline,
                )
                for shipping_object in shipping_objects
            ]
        return []

    async def create_shipping(self, shipping_input: ShippingInputDTO) -> Shipping:
        shipping = await self.repository.save(shipping_input)
        return shipping
