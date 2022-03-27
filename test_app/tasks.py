from fastapi import Depends, HTTPException, status
from typing import List

from test_app.database import get_session
from test_app.schemas import *
from test_app.models import *


class TaskService:
    def __init__(self, session=Depends(get_session)):
        self.session = session

    def get_tasks(self) -> List[Task]:
        tasks = self.session.query(TaskModel).all()
        return tasks

    def create_task(self, task_data: Task) -> TaskModel:
        task = TaskModel(**task_data.dict())
        self.session.add(task)
        self.session.commit()
        return task

    def update_task(self, task_id, task_data: BaseTask) -> TaskModel:
        task = self.session.query(TaskModel).filter(TaskModel.task_uuid == task_id).first()
        if not task:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            for field, value in task_data.dict().items():
                setattr(task, field, value)
            self.session.commit()
        return task
