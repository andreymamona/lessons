from sqlalchemy import create_engine, update, select
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import inspect
from models import *
from utils import *
import logging

logger = logging.getLogger(__name__)
engine = setup_db_engine()
inspector = inspect(engine)
schemas = inspector.get_schema_names()

def admin_menu(session):
    while True:
        logger.info(f'* 1-add user, 2-edit data, 3-delete user, 4-random, 5-show all,'
                    f' 6-add product, 7-new purchase, 8-find user, 9-custom, 0-stop program'
                    f'\n* Choose your action: ')
        choice = input()
        if choice == '0':
            return
        elif choice == '1':
            add_user(session)
        elif choice == '2':
            edit_user(session)
        elif choice == '3':
            delete_user(session)
        elif choice == '4':
            num = int(input('Input quantity of new random users: '))
            random_addition(session, num)
        elif choice == '5':
            list_of_users = show_all_users(session)
            try:
                while True:
                    logger.info(next(list_of_users))
            except:
                logger.info('End of list')
        elif choice == '6':
            add_new_product(session)
        elif choice == '7':
            add_new_purchase(session)
        elif choice == '8':
            f = find_user_by_email(session)
            for u in f:
                print(u.id, u.email, u.password)
        elif choice == '9':
            schema = 'public'
            for table_name in inspector.get_table_names(schema=schema):  # add 'for schema in schemas' to view all
                logger.info(f"Table: {table_name}")
                logger.info(list(column['name'] for column in inspector.get_columns(table_name, schema=schema)))
        else:
            logger.info('Wrong choice!!! Try again!')
            pass


def user_menu(session):
    logger.info('Yor are looser')

