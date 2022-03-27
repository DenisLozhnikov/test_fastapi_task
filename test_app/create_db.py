from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os


def init_db():
    engine = create_engine(os.getenv('DATABASE_URL'))
    session = Session(bind=engine.connect(), autocommit=True)

    session.execute("""create table if not exists tasks_table (
    task_uuid uuid,
    description varchar(256),
    params json
    );""")

    session.close()


if __name__ == '__main__':
    init_db()
