
from sqlalchemy.orm import sessionmaker
from models import Base, User, Address, Profile #, Purchase, Product
from utils import setup_db_engine, create_database_if_not_exists


if __name__ == '__main__':
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(email="test73@test.com", password="password4")
    session.add(user)

    session.commit()

    address = Address(user_id=user.id, city="Minsk", address="Test")
    session.add(address)
    profile = Profile(user_id=user.id, phone="+37533667141", age=34)
    session.add(profile)

    session.commit()


