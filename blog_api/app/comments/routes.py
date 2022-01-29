from flask import Blueprint, request
from ..util.api_response import *
from ..util.decorators import token_auth
from ..managers.commentmanager import CommentManager
from ..models import Comment


comment = Blueprint('comment', __name__)


@comment.route('/comments/', methods=['POST'])
@token_auth
def create_comment():
    data = request.get_json()['data']

    new_comment = Comment(user_id=data['user_id'], post_id=data['post_id'], content=['content'])
    CommentManager.save(new_comment)
    return success_response()


@comment.route('/comments/<comment_id>/delete', methods=['POST'])
@token_auth
def delete_comment(comment_id):
    data = request.get_json()['data']
    comment = CommentManager.get_by_id(comment_id)
    
    if not comment:
        return not_found("Comment not found!")

    #check if user deleting comment is valid
    if comment.user_id != data['user_id']:
        return unauthorized_request()

    CommentManager.delete(comment)
    return success_response()
    
