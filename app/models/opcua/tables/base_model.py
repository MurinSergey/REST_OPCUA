from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel as PyBaseModel, Field
from typing_extensions import Annotated

class BaseModel(PyBaseModel):
    id: Annotated[int, Field(default_factory=lambda: uuid4().hex)]
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]

