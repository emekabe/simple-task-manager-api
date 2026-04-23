from sqlalchemy.orm import Session
from app.models.task import Task


def create_task(db: Session, title: str, description: str | None):
    task = Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task: Task, updates: dict):
    for key, value in updates.items():
        if value is not None:
            setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
