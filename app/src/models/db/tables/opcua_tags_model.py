from .base_model import BaseModel
from datetime import datetime
from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

class OpcuaTagModel(BaseModel):
    tag_name: Mapped[str] = mapped_column(unique=True)
    opcua_node: Mapped[str]
    activated: Mapped[bool] = mapped_column(default=False)
    archive: Mapped[bool] = mapped_column(default=False)
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )