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
	post.year= request.form.get("year")
	post.title= request.form.get("title")
	post.text= request.form.get("text")
	post.url= request.form.get("url")

	y1_cs=request.form.get("Y1-CS")
	if y1_cs==True:
		post.y1_cs=True

	else:
		post.y1_cs=False

	y1_entrep=request.form.get("Y1-E")
	if y1_entrep==True:
		post.y1_entrep=True

	else:
		post.y1_entrep=False


	y2_cs=request.form.get("Y2-CS")
	if y2_cs==True:
		post.y2_cs=True

	else:
		post.y2_cs=False


	y2_entrep=request.form.get("Y2-E")
	if y2_entrep==True:
		post.y2_entrep=True

	else:
		post.y2_entrep=False

	y3_cs=request.form.get("Y3-CS")
	if y3_cs==True:
		post.y3_cs=True

	else:
		post.y3_cs=False

	y3_entrep=request.form.get("Y3-E")
	if y3_entrep==True:
		post.y3_entrep =True

	else:
		post.y3_entrep=False

	session.add(post)
	session.commit()

	return render_template('add_post.html')


@app.route('/year/<int:year>')
def years(year):
	# query the database to get that year's content
	cs_posts = session.query(Post).filter_by(year=year, topic="cs").all()
	entrep_posts = session.query(Post).filter_by(year=year, topic="entrep").all()
	return render_template("years.html", cs_posts= cs_posts, entrep_posts= entrep_posts, year=year)
	#return render_template("years.html", year= year)

@app.route('/Y1')
def y1():
	return render_template('Y1.html')

@app.route('/Y2')
def y2():
	return render_template('Y2.html')

@app.route('/Y3')
def y3():
	return render_template('Y3.html')

@app.route('/protected', methods=["GET"])
@login_required
def protected():
	return render_template('protected.html')

@app.route('/stylesheet')
def style():
	return render_template('stylesheet.html')

# @app.route('/add-random-post')
# def add_something():
# 	post = Post()
# 	post.year=3
# 	post.topic="entrep"
# 	post.title="random entrep post"
# 	post.text='random post text'
# 	session.add(post)
# 	session.commit()
# 	return("<h1>Done</h1>")


###### LOGIN #######

@app.route('/login', methods=['GET', 'POST'])
def login():
	return login_handler(request)

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
	name = request.form.get(name)
	email = request.form.get(email)
	pw = request.form.get(pw_hash)
	member=request.form.get(member)


	return render_template('sign_up.html')

@app.route('/logout')
def logout():
  return logout_handler()
