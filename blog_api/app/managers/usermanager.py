from basemanager import BaseManager
from ..models import User


class UserManager(BaseManager):
    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def get_by_email(user_email):
        return User.query.filter_by(email=user_email).first()

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()