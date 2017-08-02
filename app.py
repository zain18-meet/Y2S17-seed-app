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

@app.route('/home')
def home():
	return render_template('home.html')



@app.route('/add_post', methods=['GET', 'POST'])
def add_post():

	post = Post()
	post.year= session.query(Post)
	post.title= session.query(Post)
	post.text= session.query(Post)
	post.url= session.query(Post)

	return render_template('add_post.html')


@app.route('/year/<int:year>')
def years(year):
	# query the database to get that year's content
	cs_posts = session.query(Post).filter_by(year=year, topic="cs").all()
	entrep_posts = session.query(Post).filter_by(year=year, topic="entrep").all()
	return render_template("years.html", cs_posts= cs_posts, entrep_posts= entrep_posts, year=year)
	#return render_template("years.html", year= year)

@app.route('/protected', methods=["GET"])
@login_required
def protected():
	return render_template('protected.html')

@app.route('/add-random-post')
def add_something():
	post = Post()
	post.year=3
	post.topic="entrep"
	post.title="random entrep post"
	post.text='random post text'
	session.add(post)
	session.commit()
	return("<h1>Done</h1>")


###### LOGIN #######

@app.route('/login', methods=['GET', 'POST'])
def login():
	return login_handler(request)

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
	return render_template('sign_up.html')

@app.route('/logout')
def logout():
  return logout_handler()
