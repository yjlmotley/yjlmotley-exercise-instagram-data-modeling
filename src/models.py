import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class PostDisike(Base): 
    __tablename__ = 'Post Dislike'
    id = Column(Integer, primary_key=True)
    postID = Column(Integer, ForeignKey('Post.id'))
    dislike = Column(Boolean, nullable=False)
    count = Column(Integer)

class PostLike(Base): 
    __tablename__ = 'Post Like'
    id = Column(Integer, primary_key=True)
    postID = Column(Integer, ForeignKey('Post.id'))
    like = Column(Boolean, nullable=False)
    count = Column(Integer)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    post_text = Column(String(150), nullable=False)
    # content = 
    user_id = Column(Integer, ForeignKey('User.id'))
    comment_id = Column(Integer, ForeignKey('Comment.id'))

class CommentDisike(Base): 
    __tablename__ = 'Comment Dislike'
    id = Column(Integer, primary_key=True)
    commentID = Column(Integer, ForeignKey('Comment.id'))
    dislike = Column(Boolean, nullable=False)
    count = Column(Integer)

class CommentLike(Base): 
    __tablename__ = 'Comment Like'
    id = Column(Integer, primary_key=True)
    commentID = Column(Integer, ForeignKey('Comment.id'))
    like = Column(Boolean, nullable=False)
    count = Column(Integer)

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    followerID = Column(Integer, ForeignKey('Follower.id'))
    email = Column(String(250), nullable=False)

class FollowRequest(Base):
    __tablename__ = 'Follow Request'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('User.id'))
    followerID = Column(Integer, ForeignKey('Follower.id'))
    followedID = Column(Integer, ForeignKey('Followed.id'))
    Accepted = Column(Boolean, nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
