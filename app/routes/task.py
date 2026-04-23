from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services import task_service
from app.dependencies.db import get_db

router = APIRouter()


@router.post("/", response_model=TaskResponse)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task.title, task.description)


@router.get("/", response_model=list[TaskResponse])
def get_all(db: Session = Depends(get_db)):
    return task_service.get_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
def get_one(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update(task_id: int, updates: TaskUpdate, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task_service.update_task(db, task, updates.dict())


@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task_service.delete_task(db, task)
    return {"message": "Task deleted"}
