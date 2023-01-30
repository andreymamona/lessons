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


def product_edit():
    with sqlite3.connect("my_db.sqlite3") as session:
        product_id = input('Input product ID:')
        cursor = session.cursor()
        if product_id == 'exit':
            return
        choice = input('Choose what to change (1:name, 2:cost, 3:quantity, 4:comment or "exit":')
        if choice == 'exit':
            return
        elif choice == '1':
            value = input('Input product_name:')  # product_name
            cursor.execute(
                """
                UPDATE products SET product_name = ?
                WHERE id = ?;
                """,
                (value, product_id),
            )
            session.commit()
        elif choice == '2':
            while True:
                try:
                    value = float(input('Input cost:')) # cost
                except:
                    logger.info("Try again")
                else:
                    cursor.execute(
                        """
                        UPDATE products SET cost = ?
                        WHERE id = ?;
                        """,
                        (value, product_id),
                    )
                    session.commit()
                    break
        elif choice == '3':
            while True:
                try:
                    value = int(input('Input quantity:')) # quantity
                except:
                    logger.info("Try again")
                else:
                    cursor.execute(
                        """
                        UPDATE products SET quantity = ?
                        WHERE id = ?;
                        """,
                        (value, product_id),
                    )
                    session.commit()
                    break
        elif choice == '4':
            value = input('Input comment:') # comment
            cursor.execute(
                """
                UPDATE products SET comment = ?
                WHERE id = ?;
                
                """,
                (value, product_id),
            )
            session.commit()
        else:
            print('Wrong value!')
            return


def product_remove():
    with sqlite3.connect("my_db.sqlite3") as session:
        product_id = input('Input product ID for deletion:')
        cursor = session.cursor()
        try:
            cursor.execute(
                """
                DELETE
                FROM products
                WHERE id = ?
                ;
                """,
                (product_id)
            )
            session.commit()
            logger.info("Query executed successfully")
            all_items = cursor.fetchall()
            for row in range(len(all_items)):
                logger.info(all_items[row])
        except Error as e:
            logger.info(f"The error '{e}' occurred")


if __name__ == "__main__":
    while True:
        choice = input('Choose action (1:create table, 2:add product, 3:remove product, 4:edit product, 5:show all)')
        if choice == 1:
            create_table()
        if choice == 2:
            product_add()
        if choice == 3:
            product_remove()
        if choice == 4:
            product_edit()
        if choice == 5:
            show_all_products()









