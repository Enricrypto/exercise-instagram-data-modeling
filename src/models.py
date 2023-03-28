import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__= 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, nullable=False)
    user_to_id = Column(Integer, nullable=False)

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    password = Column(String(20), nullable=False)
    username = Column(String(10))

class Post(Base): 
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    content = Column(String(250))

class Likes(Base):
    __tablename__= 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)

class Media(Base): 
    __tablename__= 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey('post.id'))
    post = relationship(Post)
    type = Column(String(20))
    url = Column (String(250))

class Comment(Base): 
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)
    content = Column(String(150), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
