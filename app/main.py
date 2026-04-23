from fastapi import FastAPI
from app.routes import task
from app.db import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(task.router, prefix="/tasks", tags=["Tasks"])
