import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_health_check_should_return_status_200(client):
    url = "/health_check"
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_health_check_should_return_message(client):
    url = "/health_check"
    response = await client.get(url)
    data = response.json()

    assert data["message"] == "I'm OK"
