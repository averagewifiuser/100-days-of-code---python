from flask import request
from functools import wraps
from .api_response import unauthorized_request, bad_request
import jwt
import os
from ..managers.usermanager import UserManager

#TODO: make this dynamic plx
authorized_emails = ['joeajnr@blogapi.com']

def token_auth(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        bearer = request.headers.get('Authorization')
        if bearer:
            token = bearer.split()[1]
            try:
                user = jwt.decode(token, key=os.getenv('SECRET_KEY'), algorithms=['HS256', ])
                if user['email'] not in authorized_emails:
                    return unauthorized_request()
            except jwt.ExpiredSignatureError as e:
                return bad_request(str(e))
            except Exception as e:
                return bad_request(str(e))
        else:
            return unauthorized_request()
        return func(*args, **kwargs)
    return decorated_function