from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TaskModel(Base):
    __tablename__ = 'tasks_table'

    task_uuid = Column(String(40), primary_key=True)
    description = Column(String(120))
    params = Column(JSON)

