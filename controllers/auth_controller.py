from sqlalchemy.orm import Session

from Model.User import User
from utils.db import SessionLocal


class AuthController:
    def __init__(self) -> None:
        self.db: Session = SessionLocal()

    def login(self, username: str, password: str) -> bool:
        user = (
            self.db.query(User)
            .filter_by(username=username, password=password, is_manager=True)
            .first()
        )
        if user:
            return user
        return None

    def register(self, username: str, password: str, email: str) -> bool:
        user = self.db.query(User).filter_by(username=username).first()
        if user:
            return False

        user = self.db.query(User).filter_by(email=email).first()
        if user:
            return False

        user = User(username=username, password=password, email=email)
        self.db.add(user)
        self.db.commit()
        return True
