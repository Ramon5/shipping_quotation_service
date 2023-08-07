from typing import Callable

import httpx
import pytest
import pytest_asyncio

from src.app import create_app
from src.config.settings import settings
from src.domains.shipping.dtos import ShippingInputDTO, ShippingOutputDTO


@pytest.fixture(autouse=True)
def config():
    settings.DB_URL = "postgresql+asyncpg://test:test@database:5432/testdb"


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
