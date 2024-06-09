from datetime import datetime
from enum import Enum

from sqlalchemy.orm import Session

from Model.Task import Task
from utils.db import SessionLocal


class TaskController:
    def __init__(self) -> None:
        self.db: Session = SessionLocal()

    def access(self, task_id: int):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        return task

    def create(
        self,
        name: str,
        description: str,
        status: Enum,
        start_date: datetime,
        end_date: datetime,
        project_id: int,
        assignee: int,
    ):
        try:
            task = Task(
                name=name,
                description=description,
                status=status,
                start_date=start_date,
                end_date=end_date,
                project_id=project_id,
                assignee=assignee,
            )
            self.db.add(task)
            self.db.commit()
            return task
        except Exception as e:
            print(e)
            return None

    def edit(
        self,
        task_id: int,
        name: str,
        description: str,
        status: Enum,
        start_date: datetime,
        end_date: datetime,
    ):
        try:
            task = self.db.query(Task).filter(Task.id == task_id).first()
            task.name = name
            task.description = description
            task.status = status
            task.start_date = start_date
            task.end_date = end_date
            self.db.add(task)
            self.db.commit()
            return task
        except Exception as e:
            print(e)
            return None

    def delete(self, task_id: int):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        self.db.delete(task)
        self.db.commit()
        return True

    def search(self, keyword: str, project_id: int):
        list_task = (
            self.db.query(Task)
            .filter(Task.name.like(f"%{keyword}%"), Task.project_id == project_id)
            .all()
        )
        return list_task
