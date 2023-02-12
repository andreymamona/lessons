import logging
from sqlalchemy.orm import sessionmaker
from services import *
from utils import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    admin = {'admin': 'admin', 'root': 'pass'}
# Добавить возможность новой регистрации пользователя с начального экрана
    while True:

        logger.info('Enter login(email) and password separated by a space; 0 for exit')
        first_inp = input()
        if first_inp == '0':
            break
        try:
            log_email, pswd = first_inp.split(' ')
        except Exception:
            logger.info('Invalid input')
            continue
        log_email.lower()
        if log_email in admin.keys():
            if admin[log_email] == pswd:
                logger.info('You are Admin')
                admin_menu(session)
                continue
        current_user = find_user_by_email(session, log_email, pswd)
        if current_user is None:
            logger.info('Incorrect login or/and password')
            continue
        user_menu(session)
        continue

# regexp for command.col_name=val : 1: r"^[a-z]*"gm 2:r"[a-z].[a-z]+="gm 3:"=[a-z.@_ 0-9]*"
#            list_us_prod = session.query(Purchase).filter(Purchase.product_id == '2').all()
#         us_dict = {}
#         for it in list_us_prod:
#             it_name = it.product.name
#             if it.user.email in us_dict.keys():
#                 us_dict[it.user.email] += 1
#             else:
#                 us_dict[it.user.email] = 1
#         logger.info(it_name)
#         logger.info(us_dict)

