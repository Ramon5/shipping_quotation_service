from typing import List

from cache import AsyncLRU
from sqlalchemy import and_, between
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.domains.shipping.dtos import ShippingRequestDTO
from src.domains.shipping.models import Shipping
from src.infra.database.repository.repository import Repository


class ShippingRepository(Repository[Shipping]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    @AsyncLRU()
    async def query_shipping(
        self, shipping_request: ShippingRequestDTO
    ) -> List[Shipping]:
        query_result = await self._session.execute(
            select(self._model_class).where(
                and_(
                    between(
                        shipping_request.dimension.height,
                        self._model_class.minimum_height,
                        self._model_class.maximum_height,
                    ),
                    between(
                        shipping_request.dimension.width,
                        self._model_class.minimum_width,
                        self._model_class.maximum_width,
                    ),
                )
            )
        )

        return query_result.scalars().all()
