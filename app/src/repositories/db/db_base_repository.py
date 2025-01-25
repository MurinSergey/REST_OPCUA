from abc import ABC, abstractmethod


class IAbstractDbRepository(ABC):
    @abstractmethod
    async def create():
        raise NotImplementedError
    
    @abstractmethod
    async def update():
        raise NotImplementedError
    
    @abstractmethod
    async def delete():
        raise NotImplementedError
    
    @abstractmethod
    async def get_single():
        raise NotImplementedError