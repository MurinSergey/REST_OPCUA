from .base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class OpcuaTagsArchiveModel(BaseModel):
    tag_id: Mapped[int] = mapped_column(ForeignKey("opcuanodemodels.id"))
    value: Mapped[float]