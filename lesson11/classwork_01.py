# Установить библиотеку sqlite3 в операционную систему.
# Используя консоль, создать базу sqlite3, в ней создать таблицу пользователей,
# добавить новую запись, прочитать её и удалить. Подключить базу в PyCharm.
# Создать python функцию, которая создает таблицу user, для примера использовать
# слайд №12. Запустить функцию и проверить, что создался файл базы данных.
# Создать функцию, которая позволяет добавлять данные в таблицу user. Добавить
# 5 различных записей.
# Создать функцию для поиска всех пользователей с определенным именем. Запустить
# функцию и найти хотя бы одного пользователя по имени.
# Создать функцию для поиска всех пользователей в возрасте от X до Y лет.
import sqlite3
from sqlite3 import Error
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def users_add(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_db.sqlite3") as session:
        cursor = session.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO user (firstname, lastname, email, password, age)
                VALUES (?, ?, ?, ?, ?);
                """,
                (firstname, lastname, email, password, age),
            )
            session.commit()
            logger.info("Query executed successfully")
        except Error as e:
            logger.info(f"The error '{e}' occurred")


if __name__ == "__main__":
    users = [["Andrey", "Mamona", "andrey.jbjv@gmail.com", "TestPass", 34],
             ["Nikita", "Mamona", "andrey.jbjv+1@gmail.com", "TestPass", 34],
             ["Vladimir", "Mamona", "andrey.jbjv+2@gmail.com", "TestPass", 84],
             ["Leo", "Mamona", "andrey.jbjv+3@gmail.com", "TestPass", 7],
             ["Anna", "Mamona", "andrey.jbjv+4@gmail.com", "TestPass", 32]]

    users_add(*users[i] for i in range(len(users)))
