from typing import List, Optional

from fastapi import APIRouter, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.domains.shipping.controller import ShippingController
from src.domains.shipping.dtos import (
    ShippingInputDTO,
    ShippingOutputDTO,
    ShippingRequestDTO,
)
from src.domains.shipping.repository import ShippingRepository
from src.infra.database.session import get_db_session

router = APIRouter(prefix="/shipping")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_shipping_data(
    shipping_input: ShippingInputDTO, session: AsyncSession = Depends(get_db_session)
):
    controller = ShippingController(ShippingRepository(session))
    return await controller.create_shipping(shipping_input)


@router.post("/quotation")
async def query_shipping_quotation(
    shipping_request: ShippingRequestDTO,
    session: AsyncSession = Depends(get_db_session),
) -> Optional[List[ShippingOutputDTO]]:
    controller = ShippingController(ShippingRepository(session))
    return await controller.get_shipping_quotation(shipping_request)
