from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from Model.Base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
