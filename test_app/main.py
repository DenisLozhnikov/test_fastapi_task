from fastapi import FastAPI

from test_app.tasks import *

app = FastAPI()


@app.get("/tasks", response_model=List[Task])
def get_tasks(session: TaskService = Depends()):
    return session.get_tasks()


@app.post("/tasks/add", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: Task, session: TaskService = Depends()):
    return session.create_task(task_data)


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task_data: BaseTask, session: TaskService = Depends()):
    return session.update_task(task_id, task_data)
