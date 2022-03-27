from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test_app.settings import settings

engine = create_engine(settings.db_url)
Session = sessionmaker(engine)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()