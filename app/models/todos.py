from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, ModelBaseMixinWithoutDeletedAt


class Todo(ModelBaseMixinWithoutDeletedAt, Base):
    __tablename__ = "todos"

    title: Mapped[str] = mapped_column(String(100), index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    completed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
