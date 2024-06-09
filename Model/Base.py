import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    __abstract__ = True
    __table_args__ = {"mysql_charset": "utf8mb4"}
    createdAt: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=func.current_timestamp()
    )
    updatedAt: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        onupdate=func.current_timestamp(),
        default=func.current_timestamp(),
    )

    def get_info(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
