from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists


def setup_db_engine():
    DB_USER = "jimmy"
    DB_PASSWORD = "jimmy"
    DB_NAME = "jimmy"
    DB_ECHO = True

    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=DB_ECHO,
    )
    return engine


def create_database_if_not_exists(engine):
    if not database_exists(engine.url):
        create_database(engine.url)


def find_user_by_email():
    ...


def add_user():
    ...


def edit_user():
    ...


def delete_user():
    ...


def show_user():
    ...


def show_all():
    ...