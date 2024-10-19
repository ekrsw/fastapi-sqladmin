from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from app.models.base import Base, ModelBaseMixinWithoutDeletedAt


class Tag(ModelBaseMixinWithoutDeletedAt, Base):
    __tablename__ = "tags"

    name: Mapped[str] = Column(String(100), unique=True, index=True)
