import datetime

from sqlalchemy import TIMESTAMP, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from Model.Base import Base
from utils.enums import TaskStatusEnum


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[Enum] = mapped_column(Enum(TaskStatusEnum), nullable=False)
    start_date: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=func.current_timestamp()
    )
    end_date: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=func.current_timestamp()
    )
    assignee: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), nullable=False)

    def __repr__(self):
        return f"<Task(name={self.name}, status={self.status}, start_date={self.start_date}, end_date={self.end_date})>"
