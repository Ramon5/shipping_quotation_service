import os
from typing import Callable

import httpx
import pytest
import pytest_asyncio

from src.app import create_app
from src.domains.shipping.dtos import ShippingInputDTO, ShippingOutputDTO


@pytest.fixture(autouse=True)
def config(monkeypatch):
    monkeypatch.setenv("SQLALCHEMY_SILENCE_UBER_WARNING", "1")
    os.environ["SQLALCHEMY_SILENCE_UBER_WARNING"] = "1"


@pytest_asyncio.fixture
async def client():
    async with httpx.AsyncClient(
        app=create_app(), base_url="http://localhost:8000/api/v1"
    ) as async_client:
        yield async_client


@pytest.fixture
def shipping_input() -> Callable:
    def _wrapper(rate, shipping_deadline) -> ShippingInputDTO:
        return ShippingInputDTO(
            name="test",
            shipping_rate=rate,
            minimum_height=5,
            maximum_height=102,
            minimum_width=10,
            maximum_width=100,
            shipping_deadline=shipping_deadline,
        )

    return _wrapper


@pytest.fixture
def shipping_output() -> Callable:
    def _wrapper(value, deadline) -> ShippingOutputDTO:
        return ShippingOutputDTO(name="test", value=value, shipping_deadline=deadline)

    return _wrapper
