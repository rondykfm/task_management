from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.router import task_router

Base.metadata.create_all(engine)

app = FastAPI(title="This is my Task management application")

app.include_router(task_router)
