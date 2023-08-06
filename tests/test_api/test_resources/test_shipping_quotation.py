from typing import Callable

import pytest
from fastapi import status
from httpx import AsyncClient
from pytest_mock import MockerFixture

from src.domains.shipping import repository
from src.domains.shipping.dtos import ShippingRequestDTO

pytestmark = pytest.mark.asyncio


async def test_query_shipping_quotation_should_return_status_200(
    client: AsyncClient, mocker: MockerFixture
):
    mock_db = mocker.patch.object(repository.ShippingRepository, "query_shipping")
    url = "/shipping/quotation"
    shipping_request = ShippingRequestDTO(
        dimension={"height": 100, "width": 30}, weight=400
    )
    response = await client.post(url=url, data=shipping_request.model_dump_json())

    assert response.status_code == status.HTTP_200_OK
    mock_db.assert_called_once_with(shipping_request)


async def test_query_shipping_quotation_should_return_status_422(client: AsyncClient):
    request_data = {"dimensions": {"any": 4, "something": 2}}
    url = "/shipping/quotation"
    response = await client.post(url=url, data=request_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


async def test_create_shipping_data_should_return_status_200(
    client: AsyncClient, mocker: MockerFixture, shipping_input: Callable
):
    mock_db = mocker.patch.object(repository.ShippingRepository, "save")
    request_data = shipping_input(0.2, 4)
    mock_db.return_value = request_data
    url = "/shipping/"
    response = await client.post(url=url, data=request_data.model_dump_json())
    assert response.status_code == status.HTTP_201_CREATED
