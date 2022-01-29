from .extensions import db
from datetime import datetime


class AbstractModel(db.Model):
    '''
    Abstract Model which contains blueprint that are generic blueprint for 
    fields in the models
    '''
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)


class User(AbstractModel):
    __tablename__ = 'user'

    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin','member'), nullable=False, server_default="member")

    def __repr__(self):
        return f'<User {self.username}>'


class Post(AbstractModel):
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post<'{self.title}', '{self.date_posted}'>"


class Comment(AbstractModel):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Comment<'{self.id}', 'Post - {self.post_id}'>"




    
