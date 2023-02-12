import logging
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from sql_utils import *
from sql_models import *

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

engine = setup_db_engine()
create_database_if_not_exists(engine=engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        logger.info('Обрабатываю POST запрос')
        return request.form.to_dict()
    logger.info('Обрабатываю GET запрос')
    for key, value in request.args.to_dict().items():
        logger.info(f'{key} = {value}')
    return request.args.to_dict()


# страница, которая будет отображать все книги в базе данных
# Эта функция работает в режиме чтения.
@app.route('/')
@app.route('/users')
def show_users():
    users = session.query(User).all()
    return render_template("users.html", users=users)


@app.route('/users/add/', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        new_us = User(email=request.form['email'], password=request.form['password'])
        session.add(new_us)
        session.commit()
        return redirect(url_for('show_users'))
    else:
        return render_template('add_user.html')


@app.route("/users/edit/<int:user_id>", methods=['GET', 'POST'])
def edit_user(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    if request.method == 'POST':
        user.email = request.form['email']
        user.password = request.form['password']
        session.add(user)
        session.commit()
        return redirect(url_for('show_users'))
    else:
        return render_template('edit_user.html', user=user)


@app.route('/users/delete/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user_to_delete = session.query(User).filter_by(id=user_id).one()
    if request.method == 'POST':
        session.delete(user_to_delete)
        session.commit()
        return redirect(url_for('show_users'))
    else:
        return render_template('delete_user.html', user=user_to_delete)


if __name__ == '__main__':
    app.debug = True
    app.run()

