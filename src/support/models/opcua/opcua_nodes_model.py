from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class OpcuaNodeModel(Base):
    __tablename__ = "opcua_nodes"
    id: Mapped[int] = mapped_column(primary_key=True)
    tag_name: Mapped[str]
    node_id: Mapped[str]