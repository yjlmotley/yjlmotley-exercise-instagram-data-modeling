from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class PostDisike(Base): 
    __tablename__ = 'post_dislike'
    id = Column(Integer, primary_key=True)
    postID = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    dislike = Column(Boolean, nullable=False)
    count = Column(Integer)

class PostLike(Base): 
    __tablename__ = 'post_like'
    id = Column(Integer, primary_key=True)
    postID = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    like = Column(Boolean, nullable=False)
    count = Column(Integer)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_text = Column(String(150), nullable=False)
    post_media = Column(String(512), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))

class CommentDisike(Base): 
    __tablename__ = 'comment_dislike'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    dislike = Column(Boolean, nullable=False)
    count = Column(Integer)

class CommentLike(Base): 
    __tablename__ = 'comment_like'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    like = Column(Boolean, nullable=False)
    count = Column(Integer)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)

class FollowRequest(Base):
    __tablename__ = 'follow_request'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    followed_id = Column(Integer, ForeignKey('user.id'))
    accepted = Column(Boolean, nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
