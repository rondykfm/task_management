from fastapi import APIRouter, Depends,status
from src.tasks import controller
from src.tasks.dtos import TaskSchema,TaskResponseSchema
from src.utils.db import get_db

task_router = APIRouter(prefix="/tasks")

@task_router.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db = Depends(get_db)):
    return controller.create_tasks(body, db)

@task_router.get("/all_tasks",status_code=status.HTTP_200_OK)
def get_all_task(db=Depends(get_db)):
    return controller.get_task(db)


@task_router.get("/one_get/{task_id}",status_code=status.HTTP_200_OK)
def one_get(task_id:int, db = Depends(get_db)):
    return controller.get_one_task(task_id, db)


@task_router.put("/update_task/{task_id}",status_code=status.HTTP_201_CREATED)
def update(body:TaskSchema,task_id:int, db = Depends(get_db)):
    return controller.update_task(body,task_id,db)

@task_router.delete("/delete_task/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int, db = Depends(get_db)):
    return controller.delete_task(task_id,db)
