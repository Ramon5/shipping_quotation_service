import pytest
from fastapi import Depends
from pytest_mock import MockerFixture
from sqlalchemy.ext.asyncio import AsyncSession

from src.domains.shipping.controller import ShippingController
from src.domains.shipping.dtos import (
    ShippingInputDTO,
    ShippingOutputDTO,
    ShippingRequestDTO,
)
from src.domains.shipping.repository import ShippingRepository
from src.infra.database.session import get_db_session


@pytest.fixture
def controller(session: AsyncSession = Depends(get_db_session)) -> ShippingController:
    return ShippingController(ShippingRepository(session))


@pytest.mark.parametrize(
    "rate,weight,expected_price", [(0.2, 400, 8.0), (0.3, 400, 12.0)]
)
def test_calculate_shipping_price(
    controller: ShippingController, rate: float, weight: float, expected_price: float
) -> None:
    shipping = ShippingInputDTO(
        name="test",
        shipping_rate=rate,
        minimum_height=5,
        maximum_height=102,
        minimum_width=10,
        maximum_width=100,
        shipping_deadline=4,
    )
    price = controller._calculate_shipping_price(shipping, weight)
    assert price == expected_price


@pytest.mark.asyncio
async def test_get_shipping_quotation_without_result(
    mocker: MockerFixture, controller: ShippingController
) -> None:
    mock_db = mocker.patch.object(
        ShippingRepository, "query_shipping", return_value=None
    )
    shipping_request = ShippingRequestDTO(
        dimension={"height": 102, "width": 50}, weight=400
    )
    shipping_quotation = await controller.get_shipping_quotation(shipping_request)

    assert shipping_quotation == []
    mock_db.assert_called_once_with(shipping_request)


@pytest.mark.parametrize(
    "rate,weight,deadline,expected_price",
    [(0.2, 400, 4, 8.0), (0.3, 850, 6, 25.50), (0.6, 300, 7, 18.0)],
)
@pytest.mark.asyncio
async def test_get_shipping_quotation(
    mocker: MockerFixture,
    controller: ShippingController,
    shipping_input: ShippingInputDTO,
    shipping_output: ShippingOutputDTO,
    rate: float,
    weight: int,
    deadline: int,
    expected_price: float,
) -> None:
    shipping_request = ShippingRequestDTO(
        dimension={"height": 102, "width": 50}, weight=weight
    )
    output = shipping_output(expected_price, deadline)
    mock_db = mocker.patch.object(ShippingRepository, "query_shipping")
    mock_db.return_value = [shipping_input(rate, deadline)]

    shipping_quotation = await controller.get_shipping_quotation(shipping_request)

    assert shipping_quotation == [output]
    mock_db.assert_called_once_with(shipping_request)
