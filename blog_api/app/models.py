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
        return '<User {}>'.format(self.username)

    
