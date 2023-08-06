from typing import Any, Dict, List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.infra.database.repository.base import IRepository, T


class Repository(IRepository[T]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    def __map_where_clausules(self, query: Dict[str, Any]):
        clausules = []
        try:
            for key, value in query.items():
                expression = f"self._model_class.{key} == {value}"
                clausules.append(expression)
        except AttributeError:
            pass

        return ",".join(clausules)

    async def get_by_id(self, entity_id: int) -> T:
        query_result = await self._session.execute(
            select(self._model_class).where(self._model_class.id == entity_id)
        )
        return query_result.scalar_one_or_none()

    async def list_objects(self, query: Optional[Dict[str, Any]] = None) -> List[T]:
        if not query:
            query = {}

        mapped_query = self.__map_where_clausules(query)

        query_result = await self._session.execute(
            select(self._model_class).where(eval(mapped_query))
        )

        return query_result.scalars().all()

    async def save(self, entity: T) -> T:
        data = entity.model_dump(exclude_none=True)
        db_entity = self._model_class(**data)
        created_entity = await self._session.merge(db_entity)
        await self._session.commit()
        return created_entity

    async def delete(self, entity_id: int) -> bool:
        if entity := await self.get_by_id(entity_id):
            await self._session.delete(entity)
            await self._session.commit()

            return True

        return False
