from typing import Generic, Type
from .crud_base_repository import IAbstractCrudRepository
from ...models.models_type import PyModelType, CreateSchemaType

class ListRepository(IAbstractCrudRepository, Generic[PyModelType, CreateSchemaType]):

    def __init__(self, model: Type[PyModelType], db_list: list[PyModelType]):
        self._database = db_list
        self.model = model

    #Метод для получения всех записей
    async def get_all(self) -> list[PyModelType]:
        res = self._database.copy()
        return res