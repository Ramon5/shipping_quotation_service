from abc import abstractmethod
from typing import Generic, List, Optional, TypeVar

from src.infra.database.base import ITable
from src.utils.patterns import Singleton

T = TypeVar("T", bound=ITable)


class IRepository(Generic[T], metaclass=Singleton):
    def __init__(self, session) -> None:
        super().__init__()
        self._session = session
        self._model_class = self.__orig_bases__[0].__args__[0]

    def set_model(self, model_class):
        self._model_class = model_class

    @abstractmethod
    async def get_by_id(self, entity_id: int) -> T:
        pass

    @abstractmethod
    async def list_objects(self, query: Optional[str] = None) -> Optional[List[T]]:
        pass

    @abstractmethod
    async def save(self, entity: T) -> T:
        pass

    @abstractmethod
    async def delete(self, entity_id: int) -> bool:
        pass
