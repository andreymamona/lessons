from utils import *


if __name__ == '__main__':
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        choice = input(f'* 1-add user, 2-edit data, 3-delete user, 4-random, 5-show all,'
                       f' 0-stop program'
                       f'\n* Choose your action: ')
        if choice == '0':
            break
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
                    next(list_of_users)
            except:
                print('End of list')
        else:
            print('Wrong choice!!! Try again!')
            pass

