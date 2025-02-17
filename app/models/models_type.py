from typing import TypeVar
from pydantic import BaseModel as PyBaseModel
from sqlalchemy.orm import DeclarativeBase

SqlAlchemyModelType = TypeVar("SqlAlchemyModelType", bound=DeclarativeBase) # Может быть любым подтипом от sqlalchemy.orm.DeclarativeBase
ListModelType = TypeVar("PyModelType", bound=PyBaseModel) # Может быть любым подтипом от pydantic.BaseModel

RequestSchemaType = TypeVar("RequestSchemaType", bound=PyBaseModel)  # Может быть любым подтипом от pydantic.BaseModel
CreateSchemaType = TypeVar("CreateSchemaType", bound=PyBaseModel)  # Может быть любым подтипом от pydantic.BaseModel
ResponseSchemaType = TypeVar("ResponseSchemaType", bound=PyBaseModel)  # Может быть любым подтипом от pydantic.BaseModel