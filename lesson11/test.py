import sqlite3
from sqlite3 import Error
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def product_edit():
    with sqlite3.connect("my_db.sqlite3") as session:
        product_id = input('Input product ID:')
        dif = None
        cursor = session.cursor()
        if product_id == 'exit':
            return
        choice = input('Choose what to change (1:name, 2:cost, 3:quantity, 4:comment or "exit":')
        if choice == 'exit':
            return
        elif choice == '1':
            value = input('Input product_name:')  # product_name
            dif = 'product_name'
            session.commit()
        elif choice == '2':
            while True:
                try:
                    value = float(input('Input cost:'))  # cost
                except:
                    logger.info("Try again")
                else:
                    dif = 'cost'
                    session.commit()
                    break
        elif choice == '3':
            while True:
                try:
                    value = int(input('Input quantity:'))  # quantity
                except:
                    logger.info("Try again")
                else:
                    dif = 'quantity'
                    break
        elif choice == '4':
            value = input('Input comment:')  # comment
            dif = 'comment'
        else:
            print('Wrong value!')
            return
        cursor.execute(f"""
            UPDATE products SET {dif} = {value}
            WHERE id = {product_id};
            """
        )
        session.commit()

product_edit()