from sqlalchemy.orm import Session

from Model.Project import Project
from Model.User import User
from utils.db import SessionLocal


class ProjectController:
    def __init__(self) -> None:
        self.db: Session = SessionLocal()

    def access(self, project_id: int):
        project = self.db.query(Project).filter(Project.id == project_id).first()
        return project

    def create(self, name: str, description: str, user_id: int) -> bool:
        try:
            project = Project(name=name, description=description, user_id=user_id)
            self.db.add(project)
            self.db.commit()
            return project
        except Exception as e:
            print(e)
            return None

    def search(self, keyword: str) -> Project:
        list_project = (
            self.db.query(Project).filter(Project.name.like(f"%{keyword}%")).all()
        )
        return list_project

    def edit(self, id: int, name: str, description: str):
        project = self.db.query(Project).filter(Project.id == id).first()
        project.name = name
        project.description = description
        self.db.commit()
        return True

    def delete(self, id: int):
        project = self.db.query(Project).filter(Project.id == id).first()
        self.db.delete(project)
        self.db.commit()
        return True

    def search_staff(self, keyword: str):
        list_staff = self.db.query(User).filter(User.email.like(f"%{keyword}%")).all()
        return list_staff
