from typing import AsyncGenerator

import databases
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config.settings import settings
from src.infra.database.base import ITable

database = databases.Database(settings.DB_URL)

engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=True, future=True)


async def init_db() -> None:
    await database.connect()
    async with engine.begin() as conn:
        # await conn.run_sync(ITable.metadata.drop_all)
        await conn.run_sync(ITable.metadata.create_all)


async def close_connection() -> None:
    await database.disconnect()


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
