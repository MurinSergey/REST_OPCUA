from typing import Generic, Type, List
from .crud_base_repository import IAbstractCrudRepository
from ...models.models_type import ListModelType, CreateSchemaType

class NoResultFound(Exception):

    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

class ListRepository(IAbstractCrudRepository, Generic[ListModelType, CreateSchemaType]):

    def __init__(self, model: Type[ListModelType], db_list: List[ListModelType]):
        self._database = db_list
        self.model = model

    async def __filter_by_field__(objects: List[ListModelType], **filters) -> List[ListModelType]:
        if not objects:
            raise AttributeError(f"Список {type(objects)} пуст")
        else:
            for field in filters.keys():
                if not hasattr(objects[0], field):
                    raise AttributeError(f"{type(objects[0])} не содержит поля {field}")

        res = [ obj for obj in objects if all( getattr( obj, field == value ) for field, value in filters.items() ) ]

        if not res:
            raise NoResultFound("Данные по запросу не найдены", 404)
        return res

    async def __sort_by_field__(objects: List[ListModelType], order: str, reverse: bool = False) -> List[ListModelType]:
        if not objects:
            raise AttributeError(f"Список {type(objects)} пуст")
        elif not hasattr(objects[0], order):
            raise AttributeError(f"{type(objects[0])} не содержит поля {order}")
        
        res = [ sorted(objects, key=lambda obj: getattr(obj, order),  reverse=reverse) ]
        return res

    #Метод для получения всех записей
    async def get_all(self, order: str) -> List[ListModelType]:
        res: List[ListModelType] = []
        for row in self._database:
            res.append(row.model_copy())
        res = self.__sort_by_field__(res, order)
        return res
    
    #Метод для получения одного значения по фильтру
    async def get_single(self, **filters) -> ListModelType:
        res: List[ListModelType] = []
        res = await self.__filter_by_field__(self._database, filters)
        return res[0].model_copy()

    #Медот добавления запсиси в базу
    async def create(self, data: CreateSchemaType) -> ListModelType:
        self._database.append(data.model_copy())
        return self._database[-1].model_copy()

    #Метод для обновления запсиси в базе
    async def update(self, data: CreateSchemaType, **filters) -> ListModelType:
        res: List[ListModelType] = []
        res = await self.__filter_by_field__(self._database, filters)
        for itm in res:
            for field_in, info_in in data.model_fields.items():
                if field_in in itm.model_fields.keys():
                    itm.model_fields(field_in) = info_in
        return res[0].model_copy()
    
    #Метод для удаления записи запсиси в базе
    async def delete(self, **filters) -> ListModelType:
        res: List[ListModelType] = []
        res = await self.__filter_by_field__(self._database, filters)
        result: ListModelType = res[0].model_copy()
        for itm in res:
            self._database.remove(itm)
        return result
