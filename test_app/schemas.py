from uuid import uuid4, UUID
from pydantic import BaseModel
from typing import Optional


class Params(BaseModel):
    param_1: str
    param_2: int

    class Config:
        extra = 'forbid'


class BaseTask(BaseModel):
    description: str
    params: Params


class Task(BaseModel):
    task_uuid: Optional[UUID] = uuid4()
    description: str
    params: Params

    class Config:
        orm_mode = True

