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
def home():
	return render_template('home.html')



@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
	if request.method=='GET':
		return render_template('add_post.html')
	else:
		post = Post(title=request.form.get("title"), text=request.form.get("text"),
			 url= request.form.get("url"), y1_cs=request.form.get("Y1-CS"),
			 y2_cs=request.form.get("Y2-CS"), y3_cs=request.form.get("Y3-CS"),
			 y1_entrep=request.form.get("Y1-E"), y2_entrep=request.form.get("Y2-E"),
			 y3_entrep=request.form.get("Y3-E"))
		print("adding post")
		print(request.form.get("Y1-CS"))	
		session.add(post)
		session.commit()
		return redirect(url_for('home'))





@app.route('/Y1')
def y1():
	# cs_posts = session.query(Post).filter_by(y1_cs=True).all()
	cs_posts = session.query(Post).filter_by(y1_cs=True).all()
	entrep_posts = session.query(Post).filter_by(y1_entrep=True).all()
	# entrep_posts = session.query(Post).filter_by(y1_entrep=True).all()
	print(cs_posts)
	print(entrep_posts)
	return render_template("Y1.html", cs_posts= cs_posts, entrep_posts= entrep_posts, year=1)
	

@app.route('/Y2')
def y2():
	cs_posts = session.query(Post).filter_by(y2_cs=True).all()
	entrep_posts = session.query(Post).filter_by(y2_entrep=True).all()
	# entrep_posts = session.query(Post).filter_by(y1_entrep=True).all()
	print(cs_posts)
	print(entrep_posts)
	return render_template("Y2.html", cs_posts= cs_posts, entrep_posts= entrep_posts, year=2)

@app.route('/Y3')
def y3():
	cs_posts = session.query(Post).filter_by(y3_cs=True).all()
	entrep_posts = session.query(Post).filter_by(y3_entrep=True).all()
	# entrep_posts = session.query(Post).filter_by(y1_entrep=True).all()
	print(cs_posts)
	print(entrep_posts)
	return render_template("Y3.html", cs_posts= cs_posts, entrep_posts= entrep_posts, year=3)

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
	if request.method == "GET":
		return render_template('sign_up.html')
	else:
		new_name   = request.form.get('name')
		new_email  = request.form.get('email')
		new_pw     = request.form.get('pw')
		new_userspos = request.form.get('userspos')
		
		u = User(email=new_email,name=new_name,pw_hash=new_pw,userspos=new_userspos)
		u.set_password(new_pw)
		session.add(u)
		session.commit()
		return redirect(url_for('home'))


@app.route('/logout')
def logout():
  return logout_handler()
