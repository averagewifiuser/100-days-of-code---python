from flask import Blueprint, jsonify

from ..util.api_response import success_response
from ..util.decorators import token_auth

main = Blueprint('main', __name__)


@main.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Hello'})


@main.route('/protected-route', methods=['GET'])
@token_auth
def protected_route():
    return success_response(message="You have access!")