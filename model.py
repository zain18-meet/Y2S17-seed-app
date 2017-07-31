from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class post(Base):
    __tablename__  = 'post'
    id             = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    url = Column(String)
    picture_url = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    y1_cs = Column(Boolean, default=False)
    y2_cs = Column(Boolean, default=False)
    y3_cs = Column(Boolean, default=False)
    y1_entrep = Column(Boolean, default=False)
    y2_entrep = Column(Boolean, default=False)
    y3_entrep = Column(Boolean, default=False)
    photo_album = Column(Boolean, default=False)
    announce = Column(Boolean, default=False)


    # ADD YOUR FIELD BELOW ID

# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel