# Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество,
# комментарий.
# Реализовать следующие функции для продуктов: создание, чтение,
# обновление по id, удаление по id.
# Создать программу с пользовательским интерфейсом позволяющим выбирать определенную
# функцию и вводить необходимые данные.
import sqlite3
from sqlite3 import Error
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_table():
    with sqlite3.connect("my_db.sqlite3") as session:
        cursor = session.cursor()
        try:
            cursor.execute(
                """
            CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR,
            cost REAL,
            quantity INTEGER,
            comment VARCHAR
            );
            """)
            session.commit()
            logger.info("Query executed successfully")
        except Error as e:
            logger.info(f"The error '{e}' occurred")


def product_add():
    with sqlite3.connect("my_db.sqlite3") as session:
        product_name = input('Input product name:')
        while True:
            try:
                cost = float(input('Input cost:'))
            except:
                logger.info("Try again")
            else:
                break
        while True:
            try:
                quantity = int(input('Input quantity:'))
            except:
                logger.info("Try again")
            else:
                break
        comment = input('Input comment:')
        cursor = session.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO products (product_name, cost, quantity, comment)
                VALUES (?, ?, ?, ?);
                """,
                (product_name, cost, quantity, comment),
            )
            session.commit()
            logger.info("Query executed successfully")
        except Error as e:
            logger.info(f"The error '{e}' occurred")


def show_all_products():
    with sqlite3.connect("my_db.sqlite3") as session:
        cursor = session.cursor()
        try:
            cursor.execute(
                """
                SELECT *
                FROM products
                ;
                """,

            )
            session.commit()
            logger.info("Query executed successfully")
            all_items = cursor.fetchall()
            for row in range(len(all_items)):
                logger.info(all_items[row])
        except Error as e:
            logger.info(f"The error '{e}' occurred")


if __name__ == "__main__":
    ...
    # create_table()
    # product_add()
    # show_all_products()


