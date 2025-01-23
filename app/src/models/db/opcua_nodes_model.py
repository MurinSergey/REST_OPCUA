from .base_model import Base
from sqlalchemy.orm import Mapped

class OpcuaNodeModel(Base):
    tag_name: Mapped[str]
    node_id: Mapped[str]