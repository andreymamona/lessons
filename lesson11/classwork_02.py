import sqlite3


def select_user(email: str):
    with sqlite3.connect("my_db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
           """
           SELECT *
           FROM user
           WHERE email = ?;
           """,
           (email,)
        )
        session.commit()
        return cursor.fetchone()


def age_user(email: str):
    with sqlite3.connect("my_db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
           """
           DELETE
           FROM user
           WHERE age = ?;
           """,
           (email)
        )
        session.commit()
        return cursor.fetchone()


print(select_user("andrey.jbjv@gmail.com"))

