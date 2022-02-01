from lib2to3.pytree import Base
from .basemanager import BaseManager
from ..models import Comment


class CommentManager(BaseManager):
    @staticmethod
    def get_by_id(comment_id):
        return Comment.query.filter_by(id=comment_id).first()

    @staticmethod
    def get_post_comments(post_id):
        return Comment.query.filter_by(post_id=post_id).all()