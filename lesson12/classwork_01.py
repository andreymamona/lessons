# Установить в виртуальное окружение python пакеты sqlalchemy.
# Создать функции для подключения и создания базы данных.
# Создать модели пользователя, его профиля и адреса.
# Создать программу, которая создает таблицы для моделей в базе данных и запустить.
# Создать функцию, которая позволяет создавать пользователя, его профиль и адрес.
# Добавить 5 различных записей пользователей.
# Создать функции для добавления нового и обновления существующего адреса пользователя.
# Создать функцию для поиска всех пользователей с определенным возрастом.

from sqlalchemy.orm import sessionmaker
from models import Base, User, Address, Profile #, Purchase, Product
from utils import setup_db_engine, create_database_if_not_exists

# import logging
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


if __name__ == '__main__':
    engine = setup_db_engine()
    # create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # user = User(email="test7@test.com", password="password4")
    # session.add(user)
    #
    # session.commit()
    #
    # address = Address(user_id=user.id, city="Minsk", address="Test")
    # session.add(address)
    # profile = Profile(user_id=user.id, phone="+37533667141", age=34)
    # session.add(profile)
    #
    # session.commit()

    result = session.query(Profile).filter(Profile.age >= 15).first()
    print(result)

