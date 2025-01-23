from .base_model import BaseModel
from sqlalchemy.orm import Mapped

class OpcuaNodeModel(BaseModel):
    tag_name: Mapped[str]
    node_id: Mapped[str]