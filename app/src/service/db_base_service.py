from ..repositories.db import IAbstractDbRepository
from ..models.db.tables import ModelType, CreateSchemaType, UpdateSchemaType

class BaseService():

    def __init__(self, repo: IAbstractDbRepository) -> None:
        self._repo: IAbstractDbRepository = repo
    
    async def create(self, model: CreateSchemaType) -> ModelType:
        return await self._repo.create(model.model_dump())
    
    async def update(self, model: UpdateSchemaType, **filters) -> ModelType:
        return await self._repo.update(model.model_dump(), **filters)
    
    async def delete(self, **filters) -> ModelType:
        return await self._repo.delete(**filters)
    
    async def get_single(self, **filters) -> ModelType:
        return await self._repo.get_single(**filters)