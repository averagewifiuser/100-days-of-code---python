from flask import Blueprint, request
from ..util.api_response import *
from ..managers.usermanager import UserManager
from ..models import User
from ..extensions import bcrypt
import datetime
import jwt
import os

user = Blueprint('user', __name__)


@user.route('/register/', methods=['POST'])
def register():
    data = request.get_json()['data']
    user_manager = UserManager()
    existing = user_manager.check_existing(data['username'], data['email'])
    if existing:
        return bad_request('That user is taken!')

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    new_user = User(username=data['username'], email=data['email'], name=data['name'], password=hashed_password)
    UserManager.save(new_user)
    return success_response()


@user.route('/login/', methods=['POST'])
def login():
    data = request.get_json()['data']
    user = UserManager.get_by_email(data['email'])
    if user and bcrypt.check_password_hash(user.password, data['password']):
        payload_data = {
            'email': data['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(
            payload=payload_data,
            key = os.getenv('SECRET_KEY')
        )

        response = {
            'email':data['email'],
            'auth_token':token
        }
    
    else:
        return bad_request("Wrong email/password combination")

    return success_response(data=response)