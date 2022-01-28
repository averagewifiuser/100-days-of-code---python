from flask import Blueprint, request
from ..models import Post
from ..managers.postmanager import PostManager
from ..util.api_response import *
from ..util.decorators import token_auth


post = Blueprint('post', __name__)


@post.route('/posts/', methods=['GET'])
def get_posts():
    posts = PostManager.get_all()
    if not posts:
        return not_found('You have no posts!')
    
    data=[]
    for x in posts:
        p={}
        p['title'] = x.title
        p['content'] = x.content
        p['user_id'] = x.user_id
        p['created_at'] = x.created_at
        p['id'] = x.id

        data.append(p)

    return success_response(data=data)


@post.route('/posts/<post_id>/', methods=['GET'])
def get_post(post_id):
    post = PostManager.get_by_id(post_id)
    if not post:
        return not_found('That post does not exist!')
    
    data = {
        'title': post.title,
        'content': post.content,
        'created_at': post.created_at,
        'user_id': post.user_id,
        'id': post.id
    }
    return success_response(data=data)


@post.route('/posts/user/<user_id>/', methods=['GET'])
def get_user_posts(user_id):
    posts = PostManager.get_user_posts(user_id)
    if not posts:
        return not_found('That user has no posts!')

    data=[]
    for x in posts:
        p={}
        p['title'] = x.title
        p['content'] = x.content
        p['user_id'] = x.user_id
        p['created_at'] = x.created_at
        p['id'] = x.id

        data.append(p)

    return success_response(data=data)


@post.route('/posts/', methods=['POST'])
@token_auth
def create_post():
    data = request.get_json()['data']
    for key in data:
        if data[key] == '' or data[key] == None:
            return bad_request(f"{data[key]} is a required field")

    new_post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
    PostManager.save(new_post)
    return success_response()


@post.route('/posts/<post_id>/', methods=['PUT'])
@token_auth
def update_post(post_id):
    data = request.get_json()['data']
    post = PostManager.get_by_id(post_id)
    
    if not post:
        return bad_request('Post not found!')

    #validate the user editting the post
    if post.user_id != data['user_id']:
        return unauthorized_request()

    post.title = data['title']
    post.content = data['content']
    PostManager.save(post)
    return success_response()


@post.route('/posts/<post_id>/delete/', methods=['POST'])
@token_auth
def delete_post(post_id):
    data = request.get_json()['data']
    post = PostManager.get_by_id(post_id)

    if not post:
        return bad_request('Post not found!')

    if post.user_id != data['user_id']:
        return unauthorized_request()

    PostManager.delete(post)
    return success_response()