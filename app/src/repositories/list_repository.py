from typing import Generic, Type
from .db_base_repository import IAbstractDbRepository
from ..models.models_type import OpcuaModelType, CreateSchemaType, UpdateSchemaType

class ListRepository(IAbstractDbRepository, Generic[OpcuaModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[OpcuaModelType], db_list: list[OpcuaModelType]):
        self._database = db_list
        self.model = model