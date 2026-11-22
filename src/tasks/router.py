from fastapi import APIRouter, Depends,status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.utils.helpers import is_authenticated


task_router = APIRouter(prefix="/tasks")

@task_router.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):

    return controller.create_tasks(body, db, user)

@task_router.get("/all_tasks",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def get_all_task(db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.get_task(db,user)

@task_router.get("/task_all",status_code=status.HTTP_200_OK)
def get_user_all_task(db:Session=Depends(get_db),response_model=List[TaskResponseSchema],user:UserModel = Depends(is_authenticated)):
    return controller.get_all_task(db)

@task_router.get("/one_get/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def one_get(task_id:int, db = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.get_one_task(task_id, db)


@task_router.put("/update_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def update(body:TaskSchema,task_id:int, db : Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.update_task(body,task_id,db,user)

@task_router.delete("/delete_task/{task_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int, db : Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.delete_task(task_id,db,user)
