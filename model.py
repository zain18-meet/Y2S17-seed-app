import datetime 

from flask_login import UserMixin

from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class User(UserMixin, Base):
    __tablename__ = 'user'
    id            = Column(Integer, primary_key=True)
    email         = Column(String)
    pw_hash       = Column(String)
    authenticated = Column(Boolean, default=False)

    def __repr__(self):
      return "<User: %s, password: %s>" % (
        self.email, self.pw_hash)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


class Post(Base):
    __tablename__  = 'post'
    id             = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    y1_cs = Column(Boolean, default=False)
    y2_cs = Column(Boolean, default=False)
    y3_cs = Column(Boolean, default=False)
    y1_entrep = Column(Boolean, default=False)
    y2_entrep = Column(Boolean, default=False)
    y3_entrep = Column(Boolean, default=False)


    # ADD YOUR FIELD BELOW ID

# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel