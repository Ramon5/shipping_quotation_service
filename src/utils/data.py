from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncConnection

from src.domains.shipping.models import Shipping


async def load_data(conn: AsyncConnection) -> None:
    shippings = [
        {
            "name": "Entrega Ninja",
            "shipping_rate": 0.3,
            "minimum_height": 10,
            "maximum_height": 200,
            "minimum_width": 6,
            "maximum_width": 140,
            "shipping_deadline": 6,
        },
        {
            "name": "Entrega Kabum",
            "shipping_rate": 0.2,
            "minimum_height": 5,
            "maximum_height": 140,
            "minimum_width": 13,
            "maximum_width": 125,
            "shipping_deadline": 4,
        },
    ]
    await conn.execute(insert(Shipping), shippings)
    await conn.commit()
