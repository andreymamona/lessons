from pathlib import Path
from sqlalchemy import create_engine, update, select
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker
from models import *
import random
import pandas as pd


def setup_db_engine():
    DB_USER = "jimmy"
    DB_PASSWORD = "jimmy"
    DB_NAME = "jimmy"
    DB_ECHO = False

    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=DB_ECHO,
    )
    return engine


def create_database_if_not_exists(engine):
    if not database_exists(engine.url):
        create_database(engine.url)


def find_user_by_email():
    ...


def add_user(session):
    new_email = input('Input email for new user:')
    new_pass = input('Input password for new user:')
    user = User(email=new_email, password=new_pass)
    session.add(user)
    session.commit()
    new_city = input('Input city for new user:')
    new_addr = input('Input address for new user:')
    address = Address(user_id=user.id, city=new_city, address=new_addr)
    new_phone = input('Input phone number for new user:')
    new_age = input('Input age for new user:')
    profile = Profile(user_id=user.id, phone=new_phone, age=new_age)
    session.add(profile, address)

    session.commit()


def edit_user(session):
    num = int(input('Input user ID for editing:'))
    address = session.query(Address).filter(Address.user_id == num).first()
    profile = session.query(Profile).filter(Profile.user_id == num).first()
    user = session.get(User, num)
    print(f'{user.id} {user.email} Pswd:{user.password} Address: {address.city} {address.address} Age:{profile.age}'
          f' tel:{profile.phone}')
    choice = input('Edit user data-1, profile-2, address-3, cancel-0:')
    if choice == '1':
        session.execute(update(User).where(User.id == num).values(email=input('Input email:')))
        session.execute(update(User).where(User.id == num).values(password=input('Input password:')))
    elif choice == '2':
        session.execute(update(Profile).where(Profile.user_id == num).values(phone=input('Input phone:')))
        session.execute(update(Profile).where(Profile.user_id == num).values(age=input('Input age:')))
    elif choice == '3':
        session.execute(update(Address).where(Address.user_id == num).values(city=input('Input city:')))
        session.execute(update(Address).where(Address.user_id == num).values(address=input('Input address:')))
    elif choice == '0':
        return
    else:
        return print('Wrong choice!')
    session.commit()



def delete_user(session):
    num = int(input('Input user ID for deletion:'))
    address = session.query(Address).filter(Address.user_id == num).first()
    session.delete(address)
    profile = session.query(Profile).filter(Profile.user_id == num).first()
    session.delete(profile)
    user_del = session.get(User, num)
    session.delete(user_del)

    session.commit()


def show_user():
    ...


def show_all_users(session):
    list_of_users = session.query(User).order_by(User.id).all()
    for user in list_of_users:
        address = session.query(Address).filter(Address.user_id == user.id).first()
        profile = session.query(Profile).filter(Profile.user_id == user.id).first()
        yield print(f'{user.id} {user.email} Address: {address.city} {address.address} Age:{profile.age}'
                    f' tel:{profile.phone}')


def random_addition(session, num):
    reader = pd.read_csv("sample.csv", header=None)
    for i in range(num):
        new_email = f'{reader[0][random.randint(0, 199)]}.{reader[1][random.randint(0, 199)]}' \
                    f'@{reader[2][random.randint(0, 199)]}'
        new_pass = reader[3][random.randint(0, 199)]
        user = User(email=new_email, password=new_pass)
        session.add(user)
        session.commit()
        new_city = reader[4][random.randint(0, 199)]
        new_addr = f'{reader[5][random.randint(0, 199)]}, {random.randint(1, 199)}'
        address = Address(user_id=user.id, city=new_city, address=new_addr)
        session.add(address)
        new_phone = f'+375-29-{random.randint(1000000, 9999999)}'
        new_age = random.randint(14, 99)
        profile = Profile(user_id=user.id, phone=new_phone, age=new_age)
        session.add(profile)
        session.commit()
