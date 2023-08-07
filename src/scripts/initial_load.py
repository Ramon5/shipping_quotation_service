import asyncclick as click

from src.domains.shipping.dtos import ShippingInputDTO
from src.domains.shipping.repository import ShippingRepository
from src.infra.database.session import async_session


@click.command()
async def load_initial_data():
    async with async_session() as session:
        repository = ShippingRepository(session)

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

        for shipping in shippings:
            model = ShippingInputDTO(**shipping)
            await repository.save(model)


if __name__ == "__main__":
    load_initial_data(_anyio_backend="asyncio")
