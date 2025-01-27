from typing import TypeVar
from pydantic import BaseModel as PyBaseModel
from .db.tables import BaseModel as SqlAlchemyBaseModel
from .opcua.tables import BaseModel as OpcuaBaseModel

SqlAlchemyModelType = TypeVar("SqlAlchemyModelType", bound=SqlAlchemyBaseModel) # Может быть любым подтипом от db.tables.BaseModel
OpcuaModelType = TypeVar("OpcuaModelType", bound=OpcuaBaseModel) # Может быть любым подтипом от opcua.tables.BaseModel
ResponseSchemaType = TypeVar("ResponseSchemaType", bound=PyBaseModel)  # Может быть любым подтипом от pydantic.BaseModel
CreateSchemaType = TypeVar("CreateSchemaType", bound=PyBaseModel)  # Может быть любым подтипом от pydantic.BaseModel
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PyBaseModel)  # Может быть любым подтипом от pydantic.BaseModel