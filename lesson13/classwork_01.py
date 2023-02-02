
from sqlalchemy.orm import sessionmaker
from models import Base, User, Address, Profile, Purchase, Product
from utils import setup_db_engine, create_database_if_not_exists


if __name__ == '__main__':
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        choice = input(f'* 1-add user, 2-edit user data, 3-delete user, 4-show user, 5-show all,'
                       f' 0-stop program'
                       f'\n* Choose your action: ')

        if choice == '0':
            break
        elif choice == '1':
            ...
        elif choice == '2':
            ...
        elif choice == '3':
            ...
        elif choice == '4':
            ...
        elif choice == '5':
            ...
        else:
            print('Wrong choice!!! Try again!')
            pass

    # user = User(email="test473@test.com", password="password4")
    # session.add(user)
    #
    # session.commit()
    #
    # address = Address(user_id=user, city="Minsk", address="Test")
    # session.add(address)
    # profile = Profile(user_id=user, phone="+37533667141", age=34)
    # session.add(profile)
    #
    # session.commit()
