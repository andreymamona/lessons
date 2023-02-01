# Установить в виртуальное окружение python пакеты sqlalchemy.
# Создать функции для подключения и создания базы данных.
# Создать модели пользователя, его профиля и адреса.
# Создать программу, которая создает таблицы для моделей в базе данных и запустить.
# Создать функцию, которая позволяет создавать пользователя, его профиль и адрес.
# Добавить 5 различных записей пользователей.
# Создать функции для добавления нового и обновления существующего адреса пользователя.
# Создать функцию для поиска всех пользователей с определенным возрастом.

# from pathlib import Path
# from sqlalchemy import create_engine
# from sqlalchemy_utils import create_database, database_exists
# from sqlalchemy import Integer, String, Column, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from models import Base, User  # , Profile, Address
from utils import setup_db_engine, create_database_if_not_exists

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(email="test2@test.com", password="password")
    session.add(user)
    session.commit()
