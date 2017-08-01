# flask imports
from flask import Flask, Response, render_template, request, redirect, url_for

# flask setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "ITSASECRET"

# flask-login imports
from flask_login import login_required, current_user
from login import login_manager, login_handler, logout_handler
login_manager.init_app(app)

# SQLAlchemy
from model import Base, Post, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/post', methods=['GET', 'POST'])
def add_post():
    return render_template('add_post.html')


@app.route('/year/<string:year>')
def years(year):
	render_template("years.html", year = year)


@app.route('/protected', methods=["GET"])
@login_required
def protected():
    return render_template('protected.html')


###### LOGIN #######

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_handler(request)


@app.route('/logout')
def logout():
  return logout_handler()
