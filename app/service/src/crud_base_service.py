from abc import ABC, abstractmethod

class IAbstractCrudService(ABC):
    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def get_single(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def delete(self, **kwargs):
        raise NotImplementedError