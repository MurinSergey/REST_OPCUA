from datetime import datetime
from uuid import uuid4
from pydantic import Field
from asyncua.ua import status_codes
from typing_extensions import Annotated
from .base_model import BaseModel

class OpcuaCurrentValue(BaseModel):
    tag_name: Annotated[str, Field(default_factory=lambda: f"NewTag_{uuid4().hex}")]
    opcua_node: Annotated[str, Field(default_factory=lambda: f"NewNode_{uuid4().hex}")]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    status_code: Annotated[str, Field(default_factory=lambda: hex(status_codes.StatusCodes.Uncertain))]
    status_str: Annotated[str, Field(default_factory=lambda: ". ".join(status_codes.code_to_name_doc[status_codes.StatusCodes.Uncertain]))]


if __name__ == "__main__":
    vls = OpcuaCurrentValue()
    print(vls.model_dump())