from typing import Generic, List
from .crud_base_service import IAbstractCrudService
from ...repositories import IAbstractCrudRepository
from ...models.models_type import CreateSchemaType, ResponseSchemaType

class SqlAlchemyService(IAbstractCrudService, Generic[CreateSchemaType, ResponseSchemaType]):

    def __init__(self, repo: IAbstractCrudRepository) -> None:
        self._repo: IAbstractCrudRepository = repo
    
    async def create(self, model: CreateSchemaType) -> ResponseSchemaType:
        return await self._repo.create(model.model_dump())
    
    async def get_single(self, **filters) -> ResponseSchemaType:
        return await self._repo.get_single(**filters)
    
    async def get_all(self, order: str) -> List[ResponseSchemaType]:
        return await self._repo.get_all(order)
    
    async def update(self, model: CreateSchemaType, **filters) -> ResponseSchemaType:
        return await self._repo.update(model.model_dump(), **filters)
    
    async def delete(self, **filters) -> ResponseSchemaType:
        return await self._repo.delete(**filters)
    
