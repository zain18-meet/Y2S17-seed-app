from flask import redirect, url_for, render_template
from flask_login import LoginManager, login_user, logout_user

import sys

from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    user = session.query(User).filter_by(id=user_id)
    if user.count() == 0:
        return
    return user.first()


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


def login_handler(request):
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('email')
    pw    = request.form.get('pw')
    user  = session.query(User).filter_by(email=email) 
    if user.count() == 1:
        user = user.first()
        if user.check_password(pw):
            login_user(user)
            return redirect(url_for('home'))
        return 'Wrong Password'
    return 'Bad login'

def sign_up_handler(request):
    new_name     = request.form.get('name')
    new_email    = request.form.get('email')
    new_pw       = request.form.get('pw')
    new_userspos = request.form.get('member')
    
    u = User(email=new_email,name=new_name,pw_hash=new_pw,userspos=new_userspos)
    u.set_password(new_pw)
    session.add(u)
    session.commit()
    login_user(u)
    return redirect(url_for('home'))


def logout_handler():
    logout_user()
    return 'Logged out'








    