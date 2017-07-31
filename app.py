# flask imports
from flask import Flask, render_template, request, redirect, url_for

# SQLAlchemy
from model import Base, YourModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup
app = Flask(__name__)
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')

@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/post', methods=['GET', 'POST'])
def add_post():
    return render_template('add_post.html') 