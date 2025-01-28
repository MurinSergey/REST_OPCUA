from typing import Generic, Type
from .crud_base_repository import IAbstractCrudRepository
from ...models.models_type import ListModelType, CreateSchemaType

class ListRepository(IAbstractCrudRepository, Generic[ListModelType, CreateSchemaType]):

    def __init__(self, model: Type[ListModelType], db_list: list[ListModelType]):
        self._database = db_list
        self.model = model

    #Метод для получения всех записей
    async def get_all(self) -> list[ListModelType]:
        res = self._database.copy()
        return res