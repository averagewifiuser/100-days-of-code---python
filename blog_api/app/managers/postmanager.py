from .basemanager import BaseManager
from ..models import Post

class PostManager(BaseManager):
    
    @staticmethod
    def get_all():
        return Post.query.all()

    @staticmethod
    def get_user_posts(user_id):
        return Post.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_id(post_id):
        return Post.query.filter_by(id=post_id).first()
    