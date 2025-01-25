from datetime import datetime
from typing import TypeVar
from pydantic import BaseModel as PyBaseModel
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

class BaseModel(DeclarativeBase):
    __abstarct__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    created_at: Mapped[datetime] = mapped_column(default=func.now())

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    
ModelType = TypeVar("ModelType", bound=BaseModel) # Может быть любым подтипом от tables.BaseModel
CreateSchemaType = TypeVar("CreateSchemaType", bound=PyBaseModel)  # Может быть любым подтипом от pydantic.BaseModel
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PyBaseModel)  # Может быть любым подтипом от pydantic.BaseModel