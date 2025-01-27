from typing import Generic
from .db_base_service import IAbstractDbService
from ..repositories import IAbstractDbRepository
from ..models.models_type import CreateSchemaType, UpdateSchemaType, ResponseSchemaType

class DbSqlAlchemyService(IAbstractDbService, Generic[CreateSchemaType, UpdateSchemaType, ResponseSchemaType]):

    def __init__(self, repo: IAbstractDbRepository) -> None:
        self._repo: IAbstractDbRepository = repo
    
    async def create(self, model: CreateSchemaType) -> ResponseSchemaType:
        return await self._repo.create(model.model_dump())
    
    async def update(self, model: UpdateSchemaType, **filters) -> ResponseSchemaType:
        return await self._repo.update(model.model_dump(), **filters)
    
    async def delete(self, **filters) -> ResponseSchemaType:
        return await self._repo.delete(**filters)
    
    async def get_single(self, **filters) -> ResponseSchemaType:
        return await self._repo.get_single(**filters)
    
    async def get_all(self) -> list[ResponseSchemaType]:
        return await self._repo.get_all()