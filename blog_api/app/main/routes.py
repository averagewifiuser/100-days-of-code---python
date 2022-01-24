from flask import Blueprint, jsonify

main = Blueprint('main', __name__)


@main.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Hello'})